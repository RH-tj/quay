# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import buildman.buildman_pb.buildman_pb2 as buildman__pb2


class BuildManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/buildman_pb.BuildManager/Ping',
                request_serializer=buildman__pb2.PingRequest.SerializeToString,
                response_deserializer=buildman__pb2.PingReply.FromString,
                )
        self.RegisterBuildJob = channel.unary_unary(
                '/buildman_pb.BuildManager/RegisterBuildJob',
                request_serializer=buildman__pb2.BuildJobArgs.SerializeToString,
                response_deserializer=buildman__pb2.BuildPack.FromString,
                )
        self.Heartbeat = channel.stream_stream(
                '/buildman_pb.BuildManager/Heartbeat',
                request_serializer=buildman__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=buildman__pb2.HeartbeatResponse.FromString,
                )
        self.SetPhase = channel.unary_unary(
                '/buildman_pb.BuildManager/SetPhase',
                request_serializer=buildman__pb2.SetPhaseRequest.SerializeToString,
                response_deserializer=buildman__pb2.SetPhaseResponse.FromString,
                )
        self.LogMessage = channel.stream_stream(
                '/buildman_pb.BuildManager/LogMessage',
                request_serializer=buildman__pb2.LogMessageRequest.SerializeToString,
                response_deserializer=buildman__pb2.LogMessageResponse.FromString,
                )
        self.DetermineCachedTag = channel.unary_unary(
                '/buildman_pb.BuildManager/DetermineCachedTag',
                request_serializer=buildman__pb2.CachedTagRequest.SerializeToString,
                response_deserializer=buildman__pb2.CachedTag.FromString,
                )


class BuildManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterBuildJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Heartbeat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPhase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LogMessage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DetermineCachedTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BuildManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=buildman__pb2.PingRequest.FromString,
                    response_serializer=buildman__pb2.PingReply.SerializeToString,
            ),
            'RegisterBuildJob': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterBuildJob,
                    request_deserializer=buildman__pb2.BuildJobArgs.FromString,
                    response_serializer=buildman__pb2.BuildPack.SerializeToString,
            ),
            'Heartbeat': grpc.stream_stream_rpc_method_handler(
                    servicer.Heartbeat,
                    request_deserializer=buildman__pb2.HeartbeatRequest.FromString,
                    response_serializer=buildman__pb2.HeartbeatResponse.SerializeToString,
            ),
            'SetPhase': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPhase,
                    request_deserializer=buildman__pb2.SetPhaseRequest.FromString,
                    response_serializer=buildman__pb2.SetPhaseResponse.SerializeToString,
            ),
            'LogMessage': grpc.stream_stream_rpc_method_handler(
                    servicer.LogMessage,
                    request_deserializer=buildman__pb2.LogMessageRequest.FromString,
                    response_serializer=buildman__pb2.LogMessageResponse.SerializeToString,
            ),
            'DetermineCachedTag': grpc.unary_unary_rpc_method_handler(
                    servicer.DetermineCachedTag,
                    request_deserializer=buildman__pb2.CachedTagRequest.FromString,
                    response_serializer=buildman__pb2.CachedTag.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'buildman_pb.BuildManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BuildManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buildman_pb.BuildManager/Ping',
            buildman__pb2.PingRequest.SerializeToString,
            buildman__pb2.PingReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterBuildJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buildman_pb.BuildManager/RegisterBuildJob',
            buildman__pb2.BuildJobArgs.SerializeToString,
            buildman__pb2.BuildPack.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Heartbeat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/buildman_pb.BuildManager/Heartbeat',
            buildman__pb2.HeartbeatRequest.SerializeToString,
            buildman__pb2.HeartbeatResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPhase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buildman_pb.BuildManager/SetPhase',
            buildman__pb2.SetPhaseRequest.SerializeToString,
            buildman__pb2.SetPhaseResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LogMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/buildman_pb.BuildManager/LogMessage',
            buildman__pb2.LogMessageRequest.SerializeToString,
            buildman__pb2.LogMessageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DetermineCachedTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buildman_pb.BuildManager/DetermineCachedTag',
            buildman__pb2.CachedTagRequest.SerializeToString,
            buildman__pb2.CachedTag.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
