# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buildman.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='buildman.proto',
  package='buildman_pb',
  syntax='proto3',
  serialized_options=b'Z)github.com/quay/quay/buildman/buildman_pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x62uildman.proto\x12\x0b\x62uildman_pb\"\r\n\x0bPingRequest\"\x1a\n\tPingReply\x12\r\n\x05reply\x18\x01 \x01(\t\"$\n\x0c\x42uildJobArgs\x12\x14\n\x0cregister_jwt\x18\x01 \x01(\t\"\xaa\x03\n\tBuildPack\x12\x0f\n\x07job_jwt\x18\x01 \x01(\t\x12\x15\n\x0bpackage_url\x18\x02 \x01(\tH\x00\x12\x38\n\x0bgit_package\x18\x03 \x01(\x0b\x32!.buildman_pb.BuildPack.GitPackageH\x00\x12\x0f\n\x07\x63ontext\x18\x04 \x01(\t\x12\x17\n\x0f\x64ockerfile_path\x18\x05 \x01(\t\x12\x12\n\nrepository\x18\x06 \x01(\t\x12\x10\n\x08registry\x18\x07 \x01(\t\x12\x12\n\npull_token\x18\x08 \x01(\t\x12\x12\n\npush_token\x18\t \x01(\t\x12\x11\n\ttag_names\x18\n \x03(\t\x12\x34\n\nbase_image\x18\x0b \x01(\x0b\x32 .buildman_pb.BuildPack.BaseImage\x1a/\n\tBaseImage\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x1a;\n\nGitPackage\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0b\n\x03sha\x18\x02 \x01(\t\x12\x13\n\x0bprivate_key\x18\x03 \x01(\tB\x0c\n\nbuild_pack\"#\n\x10HeartbeatRequest\x12\x0f\n\x07job_jwt\x18\x01 \x01(\t\"\"\n\x11HeartbeatResponse\x12\r\n\x05reply\x18\x01 \x01(\x08\"^\n\x0fSetPhaseRequest\x12\x0f\n\x07job_jwt\x18\x01 \x01(\t\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x05\x12!\n\x05phase\x18\x03 \x01(\x0e\x32\x12.buildman_pb.Phase\"<\n\x10SetPhaseResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x05\"a\n\x11LogMessageRequest\x12\x0f\n\x07job_jwt\x18\x01 \x01(\t\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x05\x12\x13\n\x0blog_message\x18\x03 \x01(\t\x12\r\n\x05phase\x18\x04 \x01(\t\">\n\x12LogMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x05\"k\n\x10\x43\x61\x63hedTagRequest\x12\x0f\n\x07job_jwt\x18\x01 \x01(\t\x12\x17\n\x0f\x62\x61se_image_name\x18\x02 \x01(\t\x12\x16\n\x0e\x62\x61se_image_tag\x18\x03 \x01(\t\x12\x15\n\rbase_image_id\x18\x04 \x01(\t\"\x1e\n\tCachedTag\x12\x11\n\tCachedTag\x18\x01 \x01(\t*d\n\x05Phase\x12\x0b\n\x07WAITING\x10\x00\x12\r\n\tUNPACKING\x10\x01\x12\x0b\n\x07PULLING\x10\x02\x12\x0c\n\x08\x42UILDING\x10\x03\x12\x0b\n\x07PUSHING\x10\x04\x12\x0c\n\x08\x43OMPLETE\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x32\xd4\x03\n\x0c\x42uildManager\x12:\n\x04Ping\x12\x18.buildman_pb.PingRequest\x1a\x16.buildman_pb.PingReply\"\x00\x12G\n\x10RegisterBuildJob\x12\x19.buildman_pb.BuildJobArgs\x1a\x16.buildman_pb.BuildPack\"\x00\x12P\n\tHeartbeat\x12\x1d.buildman_pb.HeartbeatRequest\x1a\x1e.buildman_pb.HeartbeatResponse\"\x00(\x01\x30\x01\x12I\n\x08SetPhase\x12\x1c.buildman_pb.SetPhaseRequest\x1a\x1d.buildman_pb.SetPhaseResponse\"\x00\x12S\n\nLogMessage\x12\x1e.buildman_pb.LogMessageRequest\x1a\x1f.buildman_pb.LogMessageResponse\"\x00(\x01\x30\x01\x12M\n\x12\x44\x65termineCachedTag\x12\x1d.buildman_pb.CachedTagRequest\x1a\x16.buildman_pb.CachedTag\"\x00\x42+Z)github.com/quay/quay/buildman/buildman_pbb\x06proto3'
)

_PHASE = _descriptor.EnumDescriptor(
  name='Phase',
  full_name='buildman_pb.Phase',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAITING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNPACKING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PULLING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUILDING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUSHING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1076,
  serialized_end=1176,
)
_sym_db.RegisterEnumDescriptor(_PHASE)

Phase = enum_type_wrapper.EnumTypeWrapper(_PHASE)
WAITING = 0
UNPACKING = 1
PULLING = 2
BUILDING = 3
PUSHING = 4
COMPLETE = 5
ERROR = 6



_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='buildman_pb.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=44,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='buildman_pb.PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='buildman_pb.PingReply.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=72,
)


_BUILDJOBARGS = _descriptor.Descriptor(
  name='BuildJobArgs',
  full_name='buildman_pb.BuildJobArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='register_jwt', full_name='buildman_pb.BuildJobArgs.register_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=110,
)


_BUILDPACK_BASEIMAGE = _descriptor.Descriptor(
  name='BaseImage',
  full_name='buildman_pb.BuildPack.BaseImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='buildman_pb.BuildPack.BaseImage.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='buildman_pb.BuildPack.BaseImage.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=464,
)

_BUILDPACK_GITPACKAGE = _descriptor.Descriptor(
  name='GitPackage',
  full_name='buildman_pb.BuildPack.GitPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='buildman_pb.BuildPack.GitPackage.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sha', full_name='buildman_pb.BuildPack.GitPackage.sha', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='private_key', full_name='buildman_pb.BuildPack.GitPackage.private_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=525,
)

_BUILDPACK = _descriptor.Descriptor(
  name='BuildPack',
  full_name='buildman_pb.BuildPack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_jwt', full_name='buildman_pb.BuildPack.job_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_url', full_name='buildman_pb.BuildPack.package_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='git_package', full_name='buildman_pb.BuildPack.git_package', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='buildman_pb.BuildPack.context', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dockerfile_path', full_name='buildman_pb.BuildPack.dockerfile_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repository', full_name='buildman_pb.BuildPack.repository', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registry', full_name='buildman_pb.BuildPack.registry', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pull_token', full_name='buildman_pb.BuildPack.pull_token', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='push_token', full_name='buildman_pb.BuildPack.push_token', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag_names', full_name='buildman_pb.BuildPack.tag_names', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_image', full_name='buildman_pb.BuildPack.base_image', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BUILDPACK_BASEIMAGE, _BUILDPACK_GITPACKAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='build_pack', full_name='buildman_pb.BuildPack.build_pack',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=113,
  serialized_end=539,
)


_HEARTBEATREQUEST = _descriptor.Descriptor(
  name='HeartbeatRequest',
  full_name='buildman_pb.HeartbeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_jwt', full_name='buildman_pb.HeartbeatRequest.job_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=576,
)


_HEARTBEATRESPONSE = _descriptor.Descriptor(
  name='HeartbeatResponse',
  full_name='buildman_pb.HeartbeatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='buildman_pb.HeartbeatResponse.reply', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=612,
)


_SETPHASEREQUEST = _descriptor.Descriptor(
  name='SetPhaseRequest',
  full_name='buildman_pb.SetPhaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_jwt', full_name='buildman_pb.SetPhaseRequest.job_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='buildman_pb.SetPhaseRequest.sequence_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phase', full_name='buildman_pb.SetPhaseRequest.phase', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=708,
)


_SETPHASERESPONSE = _descriptor.Descriptor(
  name='SetPhaseResponse',
  full_name='buildman_pb.SetPhaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='buildman_pb.SetPhaseResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='buildman_pb.SetPhaseResponse.sequence_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=710,
  serialized_end=770,
)


_LOGMESSAGEREQUEST = _descriptor.Descriptor(
  name='LogMessageRequest',
  full_name='buildman_pb.LogMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_jwt', full_name='buildman_pb.LogMessageRequest.job_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='buildman_pb.LogMessageRequest.sequence_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_message', full_name='buildman_pb.LogMessageRequest.log_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phase', full_name='buildman_pb.LogMessageRequest.phase', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=869,
)


_LOGMESSAGERESPONSE = _descriptor.Descriptor(
  name='LogMessageResponse',
  full_name='buildman_pb.LogMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='buildman_pb.LogMessageResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='buildman_pb.LogMessageResponse.sequence_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=871,
  serialized_end=933,
)


_CACHEDTAGREQUEST = _descriptor.Descriptor(
  name='CachedTagRequest',
  full_name='buildman_pb.CachedTagRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_jwt', full_name='buildman_pb.CachedTagRequest.job_jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_image_name', full_name='buildman_pb.CachedTagRequest.base_image_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_image_tag', full_name='buildman_pb.CachedTagRequest.base_image_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_image_id', full_name='buildman_pb.CachedTagRequest.base_image_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=935,
  serialized_end=1042,
)


_CACHEDTAG = _descriptor.Descriptor(
  name='CachedTag',
  full_name='buildman_pb.CachedTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='CachedTag', full_name='buildman_pb.CachedTag.CachedTag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1044,
  serialized_end=1074,
)

_BUILDPACK_BASEIMAGE.containing_type = _BUILDPACK
_BUILDPACK_GITPACKAGE.containing_type = _BUILDPACK
_BUILDPACK.fields_by_name['git_package'].message_type = _BUILDPACK_GITPACKAGE
_BUILDPACK.fields_by_name['base_image'].message_type = _BUILDPACK_BASEIMAGE
_BUILDPACK.oneofs_by_name['build_pack'].fields.append(
  _BUILDPACK.fields_by_name['package_url'])
_BUILDPACK.fields_by_name['package_url'].containing_oneof = _BUILDPACK.oneofs_by_name['build_pack']
_BUILDPACK.oneofs_by_name['build_pack'].fields.append(
  _BUILDPACK.fields_by_name['git_package'])
_BUILDPACK.fields_by_name['git_package'].containing_oneof = _BUILDPACK.oneofs_by_name['build_pack']
_SETPHASEREQUEST.fields_by_name['phase'].enum_type = _PHASE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
DESCRIPTOR.message_types_by_name['BuildJobArgs'] = _BUILDJOBARGS
DESCRIPTOR.message_types_by_name['BuildPack'] = _BUILDPACK
DESCRIPTOR.message_types_by_name['HeartbeatRequest'] = _HEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['HeartbeatResponse'] = _HEARTBEATRESPONSE
DESCRIPTOR.message_types_by_name['SetPhaseRequest'] = _SETPHASEREQUEST
DESCRIPTOR.message_types_by_name['SetPhaseResponse'] = _SETPHASERESPONSE
DESCRIPTOR.message_types_by_name['LogMessageRequest'] = _LOGMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['LogMessageResponse'] = _LOGMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['CachedTagRequest'] = _CACHEDTAGREQUEST
DESCRIPTOR.message_types_by_name['CachedTag'] = _CACHEDTAG
DESCRIPTOR.enum_types_by_name['Phase'] = _PHASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), {
  'DESCRIPTOR' : _PINGREPLY,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.PingReply)
  })
_sym_db.RegisterMessage(PingReply)

BuildJobArgs = _reflection.GeneratedProtocolMessageType('BuildJobArgs', (_message.Message,), {
  'DESCRIPTOR' : _BUILDJOBARGS,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.BuildJobArgs)
  })
_sym_db.RegisterMessage(BuildJobArgs)

BuildPack = _reflection.GeneratedProtocolMessageType('BuildPack', (_message.Message,), {

  'BaseImage' : _reflection.GeneratedProtocolMessageType('BaseImage', (_message.Message,), {
    'DESCRIPTOR' : _BUILDPACK_BASEIMAGE,
    '__module__' : 'buildman_pb2'
    # @@protoc_insertion_point(class_scope:buildman_pb.BuildPack.BaseImage)
    })
  ,

  'GitPackage' : _reflection.GeneratedProtocolMessageType('GitPackage', (_message.Message,), {
    'DESCRIPTOR' : _BUILDPACK_GITPACKAGE,
    '__module__' : 'buildman_pb2'
    # @@protoc_insertion_point(class_scope:buildman_pb.BuildPack.GitPackage)
    })
  ,
  'DESCRIPTOR' : _BUILDPACK,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.BuildPack)
  })
_sym_db.RegisterMessage(BuildPack)
_sym_db.RegisterMessage(BuildPack.BaseImage)
_sym_db.RegisterMessage(BuildPack.GitPackage)

HeartbeatRequest = _reflection.GeneratedProtocolMessageType('HeartbeatRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATREQUEST,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.HeartbeatRequest)
  })
_sym_db.RegisterMessage(HeartbeatRequest)

HeartbeatResponse = _reflection.GeneratedProtocolMessageType('HeartbeatResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATRESPONSE,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.HeartbeatResponse)
  })
_sym_db.RegisterMessage(HeartbeatResponse)

SetPhaseRequest = _reflection.GeneratedProtocolMessageType('SetPhaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPHASEREQUEST,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.SetPhaseRequest)
  })
_sym_db.RegisterMessage(SetPhaseRequest)

SetPhaseResponse = _reflection.GeneratedProtocolMessageType('SetPhaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPHASERESPONSE,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.SetPhaseResponse)
  })
_sym_db.RegisterMessage(SetPhaseResponse)

LogMessageRequest = _reflection.GeneratedProtocolMessageType('LogMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGEREQUEST,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.LogMessageRequest)
  })
_sym_db.RegisterMessage(LogMessageRequest)

LogMessageResponse = _reflection.GeneratedProtocolMessageType('LogMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGERESPONSE,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.LogMessageResponse)
  })
_sym_db.RegisterMessage(LogMessageResponse)

CachedTagRequest = _reflection.GeneratedProtocolMessageType('CachedTagRequest', (_message.Message,), {
  'DESCRIPTOR' : _CACHEDTAGREQUEST,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.CachedTagRequest)
  })
_sym_db.RegisterMessage(CachedTagRequest)

CachedTag = _reflection.GeneratedProtocolMessageType('CachedTag', (_message.Message,), {
  'DESCRIPTOR' : _CACHEDTAG,
  '__module__' : 'buildman_pb2'
  # @@protoc_insertion_point(class_scope:buildman_pb.CachedTag)
  })
_sym_db.RegisterMessage(CachedTag)


DESCRIPTOR._options = None

_BUILDMANAGER = _descriptor.ServiceDescriptor(
  name='BuildManager',
  full_name='buildman_pb.BuildManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1179,
  serialized_end=1647,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='buildman_pb.BuildManager.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterBuildJob',
    full_name='buildman_pb.BuildManager.RegisterBuildJob',
    index=1,
    containing_service=None,
    input_type=_BUILDJOBARGS,
    output_type=_BUILDPACK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Heartbeat',
    full_name='buildman_pb.BuildManager.Heartbeat',
    index=2,
    containing_service=None,
    input_type=_HEARTBEATREQUEST,
    output_type=_HEARTBEATRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetPhase',
    full_name='buildman_pb.BuildManager.SetPhase',
    index=3,
    containing_service=None,
    input_type=_SETPHASEREQUEST,
    output_type=_SETPHASERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LogMessage',
    full_name='buildman_pb.BuildManager.LogMessage',
    index=4,
    containing_service=None,
    input_type=_LOGMESSAGEREQUEST,
    output_type=_LOGMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DetermineCachedTag',
    full_name='buildman_pb.BuildManager.DetermineCachedTag',
    index=5,
    containing_service=None,
    input_type=_CACHEDTAGREQUEST,
    output_type=_CACHEDTAG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BUILDMANAGER)

DESCRIPTOR.services_by_name['BuildManager'] = _BUILDMANAGER

# @@protoc_insertion_point(module_scope)
