import itertools
import logging
import urllib
from collections import namedtuple
from datetime import datetime, timedelta
from math import log10

from peewee import JOIN, fn

import features
from data.cache import cache_key
from data.database import (
    IndexerVersion,
    IndexStatus,
    Manifest,
    ManifestSecurityStatus,
    db_transaction,
    get_epoch_timestamp_ms,
)
from data.registry_model import registry_model
from data.registry_model.datatypes import Manifest as ManifestDataType
from data.secscan_model.datatypes import (
    NVD,
    CVSSv3,
    Feature,
    Layer,
    Metadata,
    PaginatedNotificationResult,
    PaginatedNotificationStatus,
    ScanLookupStatus,
    SecurityInformation,
    SecurityInformationLookupResult,
    UpdatedVulnerability,
    Vulnerability,
    link_to_cves,
)
from data.secscan_model.interface import (
    InvalidConfigurationException,
    SecurityScannerInterface,
)
from util.metrics.prometheus import secscan_result_duration
from util.migrate.allocator import yield_random_entries
from util.secscan import (
    PRIORITY_LEVELS,
    fetch_vuln_severity,
    get_priority_from_cvssscore,
)
from util.secscan.blob import BlobURLRetriever
from util.secscan.v4.api import (
    APIRequestFailure,
    ClairSecurityScannerAPI,
    InvalidContentSent,
    LayerTooLargeException,
)
from util.secscan.validator import V4SecurityConfigValidator

logger = logging.getLogger(__name__)


DEFAULT_SECURITY_SCANNER_V4_REINDEX_THRESHOLD = 86400  # 1 day
TAG_LIMIT = 100

IndexReportState = namedtuple("IndexReportState", ["Index_Finished", "Index_Error"])(  # type: ignore[call-arg]
    "IndexFinished", "IndexError"
)


class ScanToken(namedtuple("NextScanToken", ["min_id"])):
    """
    ScanToken represents an opaque token that can be passed between runs of the security worker
    to continue scanning whereever the previous run left off. Note that the data of the token is
    *opaque* to the security worker, and the security worker should *not* pull any data out or modify
    the token in any way.
    """


class NoopV4SecurityScanner(SecurityScannerInterface):
    """
    No-op implementation of the security scanner interface for Clair V4.
    """

    def load_security_information(
        self, manifest_or_legacy_image, include_vulnerabilities=False, model_cache=None
    ):
        return SecurityInformationLookupResult.for_request_error("security scanner misconfigured")

    def perform_indexing(self, start_token=None, batch_size=None):
        return None

    def perform_indexing_recent_manifests(self, batch_size=None):
        return None

    def register_model_cleanup_callbacks(self, data_model_config):
        pass

    @property
    def legacy_api_handler(self):
        raise NotImplementedError("Unsupported for this security scanner version")

    def lookup_notification_page(self, notification_id, page_index=None):
        return None

    def process_notification_page(self, page_result):
        raise NotImplementedError("Unsupported for this security scanner version")

    def mark_notification_handled(self, notification_id):
        raise NotImplementedError("Unsupported for this security scanner version")

    def garbage_collect_manifest_report(self, manifest_digest):
        raise NotImplementedError("Unsupported for this security scanner version")


def maybe_urlencoded(fixed_in: str) -> str:
    """
    Handles Clair's `fixed_in_version`, which _may_ be URL-encoded.
    The API guarantee is only that the field is a string, so encoding it's
    slightly weaselly, but only slightly.
    """
    try:
        d = urllib.parse.parse_qs(fixed_in)
        # There may be additional known-good keys in the future.
        return d["fixed"][0]
    except (ValueError, KeyError):
        return fixed_in


class V4SecurityScanner(SecurityScannerInterface):
    """
    Implementation of the security scanner interface for Clair V4 API-compatible implementations.
    """

    def __init__(self, app, instance_keys, storage):
        self.app = app
        self.storage = storage

        if app.config.get("SECURITY_SCANNER_V4_ENDPOINT", None) is None:
            raise InvalidConfigurationException(
                "Missing SECURITY_SCANNER_V4_ENDPOINT configuration"
            )

        validator = V4SecurityConfigValidator(
            app.config.get("FEATURE_SECURITY_SCANNER", False),
            app.config.get("SECURITY_SCANNER_V4_ENDPOINT", None),
        )

        if not validator.valid():
            msg = "Failed to validate security scanner V4 configuration"
            logger.warning(msg)
            raise InvalidConfigurationException(msg)

        self._secscan_api = ClairSecurityScannerAPI(
            endpoint=app.config.get("SECURITY_SCANNER_V4_ENDPOINT"),
            client=app.config.get("HTTPCLIENT"),
            blob_url_retriever=BlobURLRetriever(storage, instance_keys, app),
            jwt_psk=app.config.get("SECURITY_SCANNER_V4_PSK", None),
            max_layer_size=app.config.get("SECURITY_SCANNER_V4_INDEX_MAX_LAYER_SIZE", None),
        )

    def load_security_information(
        self, manifest_or_legacy_image, include_vulnerabilities=False, model_cache=None
    ):
        if not isinstance(manifest_or_legacy_image, ManifestDataType):
            return SecurityInformationLookupResult.with_status(
                ScanLookupStatus.UNSUPPORTED_FOR_INDEXING
            )

        status = None
        try:
            status = ManifestSecurityStatus.get(manifest=manifest_or_legacy_image._db_id)
        except ManifestSecurityStatus.DoesNotExist:
            return SecurityInformationLookupResult.with_status(ScanLookupStatus.NOT_YET_INDEXED)

        if status.index_status == IndexStatus.FAILED:
            return SecurityInformationLookupResult.with_status(ScanLookupStatus.FAILED_TO_INDEX)

        if status.index_status == IndexStatus.MANIFEST_UNSUPPORTED:
            return SecurityInformationLookupResult.with_status(
                ScanLookupStatus.UNSUPPORTED_FOR_INDEXING
            )

        if status.index_status == IndexStatus.MANIFEST_LAYER_TOO_LARGE:
            return SecurityInformationLookupResult.with_status(
                ScanLookupStatus.MANIFEST_LAYER_TOO_LARGE
            )

        if status.index_status == IndexStatus.IN_PROGRESS:
            return SecurityInformationLookupResult.with_status(ScanLookupStatus.NOT_YET_INDEXED)

        assert status.index_status == IndexStatus.COMPLETED

        def security_report_loader():
            return self._secscan_api.vulnerability_report(manifest_or_legacy_image.digest)

        try:
            if model_cache:
                security_report_key = cache_key.for_security_report(
                    manifest_or_legacy_image.digest, model_cache.cache_config
                )
                report = model_cache.retrieve(security_report_key, security_report_loader)
            else:
                report = security_report_loader()
        except APIRequestFailure as arf:
            return SecurityInformationLookupResult.for_request_error(str(arf))

        if report is None:
            return SecurityInformationLookupResult.with_status(ScanLookupStatus.NOT_YET_INDEXED)

        # TODO(alecmerdler): Provide a way to indicate the current scan is outdated (`report.state != status.indexer_hash`)

        return SecurityInformationLookupResult.for_data(
            SecurityInformation(Layer(report["manifest_hash"], "", "", 4, features_for(report)))
        )

    def _get_manifest_iterator(
        self, indexer_state, min_id, max_id, batch_size=None, reindex_threshold=None
    ):
        # TODO(alecmerdler): Filter out any `Manifests` that are still being uploaded
        def not_indexed_query():
            return (
                Manifest.select(Manifest, ManifestSecurityStatus, can_use_read_replica=True)
                .join(ManifestSecurityStatus, JOIN.LEFT_OUTER)
                .where(ManifestSecurityStatus.id >> None)
            )

        def index_error_query():
            return (
                Manifest.select(Manifest, ManifestSecurityStatus, can_use_read_replica=True)
                .join(ManifestSecurityStatus)
                .where(
                    ManifestSecurityStatus.index_status == IndexStatus.FAILED,
                    ManifestSecurityStatus.last_indexed < reindex_threshold
                    or DEFAULT_SECURITY_SCANNER_V4_REINDEX_THRESHOLD,
                )
            )

        def needs_reindexing_query(indexer_hash):
            return (
                Manifest.select(Manifest, ManifestSecurityStatus, can_use_read_replica=True)
                .join(ManifestSecurityStatus)
                .where(
                    ManifestSecurityStatus.index_status != IndexStatus.MANIFEST_UNSUPPORTED,
                    ManifestSecurityStatus.index_status != IndexStatus.MANIFEST_LAYER_TOO_LARGE,
                    ManifestSecurityStatus.indexer_hash != indexer_hash,
                    ManifestSecurityStatus.last_indexed < reindex_threshold
                    or DEFAULT_SECURITY_SCANNER_V4_REINDEX_THRESHOLD,
                )
            )

        # 4^log10(total) gives us a scalable batch size into the billions.
        if not batch_size:
            batch_size = int(4 ** log10(max(10, max_id - min_id)))

        iterator = itertools.chain(
            yield_random_entries(
                not_indexed_query,
                Manifest.id,
                batch_size,
                max_id,
                min_id,
            ),
            yield_random_entries(
                index_error_query,
                Manifest.id,
                batch_size,
                max_id,
                min_id,
            ),
            yield_random_entries(
                lambda: needs_reindexing_query(indexer_state.get("state", "")),
                Manifest.id,
                batch_size,
                max_id,
                min_id,
            ),
        )

        return iterator

    def perform_indexing_recent_manifests(self, batch_size=None):
        try:
            indexer_state = self._secscan_api.state()
        except APIRequestFailure:
            return None

        if not batch_size:
            batch_size = self.app.config.get("SECURITY_SCANNER_V4_BATCH_SIZE", 0)

        reindex_threshold = datetime.utcnow() - timedelta(
            seconds=self.app.config.get("SECURITY_SCANNER_V4_REINDEX_THRESHOLD", 86400)
        )

        end_index = Manifest.select(fn.Max(Manifest.id), can_use_read_replica=True).scalar()
        if end_index is None:
            end_index = 0
        start_index = max(end_index - batch_size, 1)

        iterator = self._get_manifest_iterator(
            indexer_state,
            start_index,
            end_index,
            batch_size=max(batch_size // 20, 1),
            reindex_threshold=reindex_threshold,
        )

        self._index(iterator, reindex_threshold)

    def perform_indexing(self, start_token=None, batch_size=None):
        try:
            indexer_state = self._secscan_api.state()
        except APIRequestFailure:
            return None

        if not batch_size:
            batch_size = self.app.config.get("SECURITY_SCANNER_V4_BATCH_SIZE", 0)

        reindex_threshold = datetime.utcnow() - timedelta(
            seconds=self.app.config.get("SECURITY_SCANNER_V4_REINDEX_THRESHOLD", 86400)
        )

        max_id = Manifest.select(fn.Max(Manifest.id), can_use_read_replica=True).scalar()

        start_index = (
            start_token.min_id
            if start_token is not None
            else Manifest.select(fn.Min(Manifest.id), can_use_read_replica=True).scalar()
        )

        if max_id is None or start_index is None or start_index > max_id:
            return None

        iterator = self._get_manifest_iterator(
            indexer_state,
            start_index,
            max_id,
            batch_size=batch_size,
            reindex_threshold=reindex_threshold,
        )

        self._index(iterator, reindex_threshold)

        return ScanToken(max_id + 1)

    def _index(self, iterator, reindex_threshold):
        def mark_manifest_unsupported(manifest):
            with db_transaction():
                ManifestSecurityStatus.delete().where(
                    ManifestSecurityStatus.manifest == manifest._db_id,
                    ManifestSecurityStatus.repository == manifest.repository._db_id,
                ).execute()
                ManifestSecurityStatus.create(
                    manifest=manifest._db_id,
                    repository=manifest.repository._db_id,
                    index_status=IndexStatus.MANIFEST_UNSUPPORTED,
                    indexer_hash="none",
                    indexer_version=IndexerVersion.V4,
                    metadata_json={},
                )

        def mark_manifest_layer_too_large(manifest):
            with db_transaction():
                ManifestSecurityStatus.delete().where(
                    ManifestSecurityStatus.manifest == manifest._db_id,
                    ManifestSecurityStatus.repository == manifest.repository._db_id,
                ).execute()
                ManifestSecurityStatus.create(
                    manifest=manifest._db_id,
                    repository=manifest.repository._db_id,
                    index_status=IndexStatus.MANIFEST_LAYER_TOO_LARGE,
                    indexer_hash="none",
                    indexer_version=IndexerVersion.V4,
                    metadata_json={},
                )

        def should_skip_indexing(manifest_candidate):
            """Check whether this manifest was preempted by another worker.
            That would be the case if the manifest references a manifestsecuritystatus,
            or if the reindex threshold is no longer valid.
            """
            if getattr(manifest_candidate, "manifestsecuritystatus", None):
                return manifest_candidate.manifestsecuritystatus.last_indexed >= reindex_threshold

            return len(manifest_candidate.manifestsecuritystatus_set) > 0

        for candidate, abt, num_remaining in iterator:
            manifest = ManifestDataType.for_manifest(candidate, None)
            if manifest.is_manifest_list:
                mark_manifest_unsupported(manifest)
                continue

            layers = registry_model.list_manifest_layers(manifest, self.storage, True)
            if layers is None or len(layers) == 0:
                logger.warning(
                    "Cannot index %s/%s@%s due to manifest being invalid (manifest has no layers)"
                    % (
                        candidate.repository.namespace_user,
                        candidate.repository.name,
                        manifest.digest,
                    )
                )
                mark_manifest_unsupported(manifest)
                continue

            if should_skip_indexing(candidate):
                logger.debug("Another worker preempted this worker")
                abt.set()
                continue

            logger.debug(
                "Indexing manifest [%d] %s/%s@%s"
                % (
                    manifest._db_id,
                    candidate.repository.namespace_user,
                    candidate.repository.name,
                    manifest.digest,
                )
            )

            try:
                (report, state) = self._secscan_api.index(manifest, layers)
            except InvalidContentSent as ex:
                mark_manifest_unsupported(manifest)
                logger.exception("Failed to perform indexing, invalid content sent")
                continue
            except APIRequestFailure as ex:
                logger.exception("Failed to perform indexing, security scanner API error")
                continue
            except LayerTooLargeException as ex:
                mark_manifest_layer_too_large(manifest)
                logger.exception("Failed to perform indexing, layer too large")
                continue

            if report["state"] == IndexReportState.Index_Finished:
                index_status = IndexStatus.COMPLETED
                # record time to get results if manifest has just been uploaded
                if not manifest.has_been_scanned:
                    created_at = manifest.created_at

                    if created_at is not None:
                        dur_ms = get_epoch_timestamp_ms() - created_at
                        dur_sec = dur_ms / 1000
                        secscan_result_duration.observe(dur_sec)

                    if features.SECURITY_SCANNER_NOTIFY_ON_NEW_INDEX:
                        try:
                            vulnerability_report = self._secscan_api.vulnerability_report(
                                manifest.digest
                            )
                        except APIRequestFailure:
                            vulnerability_report = None

                        found_vulnerabilities = None
                        if vulnerability_report is not None:
                            found_vulnerabilities = vulnerability_report.get("vulnerabilities")

                        # Current implementation creates events for all detected vulnerabilities, including vulnerabilities that are low
                        # or unknown severity, which makes the whole thing a bit pointless. We'll filter out all vulnerabilities that aren't
                        # high or critical.
                        level = (
                            self.app.config.get("NOTIFICATION_MIN_SEVERITY_ON_NEW_INDEX")
                            if self.app.config.get("NOTIFICATION_MIN_SEVERITY_ON_NEW_INDEX")
                            else "High"
                        )
                        lowest_severity = PRIORITY_LEVELS[level]

                        if found_vulnerabilities is not None:
                            import notifications

                            logger.debug(
                                "Attempting to create notifications for manifest %s", manifest
                            )

                            keys = list(found_vulnerabilities)
                            for key in keys:
                                vuln = found_vulnerabilities[key]

                                found_severity = PRIORITY_LEVELS.get(
                                    vuln["normalized_severity"], PRIORITY_LEVELS["Unknown"]
                                )

                                if found_severity["score"] >= lowest_severity["score"]:
                                    tag_names = list(
                                        registry_model.tag_names_for_manifest(manifest, TAG_LIMIT)
                                    )
                                    if tag_names:
                                        event_data = {
                                            "tags": list(tag_names),
                                            "vulnerable_index_report_created": "true",
                                            "vulnerability": {
                                                "id": vuln["id"],
                                                "description": vuln["description"],
                                                "link": vuln["links"],
                                                "priority": vuln["severity"],
                                                "has_fix": bool(vuln["fixed_in_version"]),
                                            },
                                        }

                                    else:
                                        event_data = {
                                            "tags": [
                                                manifest.digest,
                                            ],
                                            "vulnerable_index_report_created": "true",
                                            "vulnerability": {
                                                "id": vuln["id"],
                                                "description": vuln["description"],
                                                "link": vuln["links"],
                                                "priority": vuln["severity"],
                                                "has_fix": bool(vuln["fixed_in_version"]),
                                            },
                                        }

                                    logger.debug(
                                        "Created notification with event_data: %s", event_data
                                    )
                                    notifications.spawn_notification(
                                        manifest.repository, "vulnerability_found", event_data
                                    )

            elif report["state"] == IndexReportState.Index_Error:
                index_status = IndexStatus.FAILED
            else:
                # Unknown state don't save anything
                continue

            with db_transaction():
                ManifestSecurityStatus.delete().where(
                    ManifestSecurityStatus.manifest == candidate
                ).execute()
                ManifestSecurityStatus.create(
                    manifest=candidate,
                    repository=candidate.repository,
                    error_json=report["err"],
                    index_status=index_status,
                    indexer_hash=state,
                    indexer_version=IndexerVersion.V4,
                    metadata_json={},
                )

    def lookup_notification_page(self, notification_id, page_index=None):
        try:
            notification_page_results = self._secscan_api.retrieve_notification_page(
                notification_id, page_index
            )

            # If we get back None, then the notification no longer exists.
            if notification_page_results is None:
                return PaginatedNotificationResult(
                    PaginatedNotificationStatus.FATAL_ERROR, None, None
                )
        except APIRequestFailure:
            return PaginatedNotificationResult(
                PaginatedNotificationStatus.RETRYABLE_ERROR, None, None
            )

        # FIXME(alecmerdler): Debugging tests failing in CI
        return PaginatedNotificationResult(
            PaginatedNotificationStatus.SUCCESS,
            notification_page_results["notifications"],
            notification_page_results.get("page", {}).get("next"),
        )

    def mark_notification_handled(self, notification_id):
        try:
            self._secscan_api.delete_notification(notification_id)
            return True
        except APIRequestFailure:
            return False

    def process_notification_page(self, page_result):
        for notification_data in page_result:
            if notification_data["reason"] != "added":
                continue

            yield UpdatedVulnerability(
                notification_data["manifest"],
                Vulnerability(
                    Severity=notification_data["vulnerability"].get("normalized_severity"),
                    Description=notification_data["vulnerability"].get("description"),
                    NamespaceName=notification_data["vulnerability"].get("package", {}).get("name"),
                    Name=notification_data["vulnerability"].get("name"),
                    FixedBy=maybe_urlencoded(
                        notification_data["vulnerability"].get("fixed_in_version")
                    ),
                    Link=notification_data["vulnerability"].get("links"),
                    Metadata={},
                ),
            )

    def register_model_cleanup_callbacks(self, data_model_config):
        pass

    @property
    def legacy_api_handler(self):
        raise NotImplementedError("Unsupported for this security scanner version")

    def garbage_collect_manifest_report(self, manifest_digest):
        def manifest_digest_exists():
            query = Manifest.select(can_use_read_replica=True).where(
                Manifest.digest == manifest_digest
            )

            try:
                query.get()
            except Manifest.DoesNotExist:
                return False

            return True

        with db_transaction():
            if not manifest_digest_exists():
                try:
                    self._secscan_api.delete(manifest_digest)
                    return True
                except APIRequestFailure:
                    logger.exception("Failed to delete manifest, security scanner API error")

        return None


def features_for(report):
    """
    Transforms a Clair v4 `VulnerabilityReport` dict into the standard shape of a
    Quay Security scanner response.
    """

    features = []
    dedupe_vulns = {}
    for pkg_id, pkg in report["packages"].items():
        pkg_env = report["environments"][pkg_id][0]
        pkg_vulns = []
        # Quay doesn't care about vulnerabilities reported from different
        # repos so dedupe them. Key = package_name + package_version + vuln_name.
        for vuln_id in report["package_vulnerabilities"].get(pkg_id, []):
            vuln_key = (
                pkg["name"]
                + "_"
                + pkg["version"]
                + "_"
                + report["vulnerabilities"][vuln_id].get("name", "")
            )
            if not dedupe_vulns.get(vuln_key, False):
                pkg_vulns.append(report["vulnerabilities"][vuln_id])
            dedupe_vulns[vuln_key] = True

        enrichments = (
            {
                key: sorted(val, key=lambda x: x["baseScore"], reverse=True)[0]
                for key, val in list(report["enrichments"].values())[0][0].items()
            }
            if report.get("enrichments", {})
            else {}
        )

        base_scores = []
        if report.get("enrichments", {}):
            for enrichment_list in report["enrichments"].values():
                for pkg_vuln in enrichment_list:
                    for k, v in pkg_vuln.items():
                        if not isinstance(v, list):
                            logger.error(f"Unexpected type for value of key '{k}': {type(v)}")
                            continue
                        for item in v:
                            if not isinstance(item, dict) or "baseScore" not in item:
                                logger.error(f"Invalid item format or missing 'baseScore': {item}")
                                continue
                            base_scores.append(item["baseScore"])

        cve_ids = [link_to_cves(v["links"]) for v in pkg_vulns]

        features.append(
            Feature(
                pkg["name"],
                "",
                "",
                pkg_env["introduced_in"],
                pkg["version"],
                base_scores,
                cve_ids,
                [
                    Vulnerability(
                        fetch_vuln_severity(vuln, enrichments),
                        vuln["updater"],
                        vuln["links"],
                        maybe_urlencoded(
                            vuln["fixed_in_version"] if vuln["fixed_in_version"] != "0" else ""
                        ),
                        vuln["description"],
                        vuln["name"],
                        Metadata(
                            vuln["updater"],
                            vuln.get("repository", {}).get("name"),
                            vuln.get("repository", {}).get("uri"),
                            vuln.get("distribution", {}).get("name"),
                            vuln.get("distribution", {}).get("version"),
                            NVD(
                                CVSSv3(
                                    enrichments.get(vuln["id"], {}).get("vectorString", ""),
                                    enrichments.get(vuln["id"], {}).get("baseScore", ""),
                                )
                            ),
                        ),
                    )
                    for vuln in pkg_vulns
                ],
            )
        )

    return features
