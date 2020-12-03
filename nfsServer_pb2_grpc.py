# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import nfsServer_pb2 as nfsServer__pb2


class NFSServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListDirectory = channel.unary_unary(
                '/NFSServer/ListDirectory',
                request_serializer=nfsServer__pb2.Path.SerializeToString,
                response_deserializer=nfsServer__pb2.FolderContents.FromString,
                )
        self.DeleteDirectory = channel.unary_unary(
                '/NFSServer/DeleteDirectory',
                request_serializer=nfsServer__pb2.Path.SerializeToString,
                response_deserializer=nfsServer__pb2.Result.FromString,
                )
        self.CreateDirectory = channel.unary_unary(
                '/NFSServer/CreateDirectory',
                request_serializer=nfsServer__pb2.Path.SerializeToString,
                response_deserializer=nfsServer__pb2.Result.FromString,
                )
        self.MoveDirectory = channel.unary_unary(
                '/NFSServer/MoveDirectory',
                request_serializer=nfsServer__pb2.SourceDestinationPath.SerializeToString,
                response_deserializer=nfsServer__pb2.Result.FromString,
                )
        self.CopyDirectory = channel.unary_unary(
                '/NFSServer/CopyDirectory',
                request_serializer=nfsServer__pb2.SourceDestinationPath.SerializeToString,
                response_deserializer=nfsServer__pb2.Result.FromString,
                )
        self.RenameDirectory = channel.unary_unary(
                '/NFSServer/RenameDirectory',
                request_serializer=nfsServer__pb2.SourceDestinationPath.SerializeToString,
                response_deserializer=nfsServer__pb2.Result.FromString,
                )


class NFSServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CopyDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RenameDirectory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NFSServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDirectory,
                    request_deserializer=nfsServer__pb2.Path.FromString,
                    response_serializer=nfsServer__pb2.FolderContents.SerializeToString,
            ),
            'DeleteDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDirectory,
                    request_deserializer=nfsServer__pb2.Path.FromString,
                    response_serializer=nfsServer__pb2.Result.SerializeToString,
            ),
            'CreateDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDirectory,
                    request_deserializer=nfsServer__pb2.Path.FromString,
                    response_serializer=nfsServer__pb2.Result.SerializeToString,
            ),
            'MoveDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveDirectory,
                    request_deserializer=nfsServer__pb2.SourceDestinationPath.FromString,
                    response_serializer=nfsServer__pb2.Result.SerializeToString,
            ),
            'CopyDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.CopyDirectory,
                    request_deserializer=nfsServer__pb2.SourceDestinationPath.FromString,
                    response_serializer=nfsServer__pb2.Result.SerializeToString,
            ),
            'RenameDirectory': grpc.unary_unary_rpc_method_handler(
                    servicer.RenameDirectory,
                    request_deserializer=nfsServer__pb2.SourceDestinationPath.FromString,
                    response_serializer=nfsServer__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NFSServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NFSServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NFSServer/ListDirectory',
            nfsServer__pb2.Path.SerializeToString,
            nfsServer__pb2.FolderContents.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NFSServer/DeleteDirectory',
            nfsServer__pb2.Path.SerializeToString,
            nfsServer__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NFSServer/CreateDirectory',
            nfsServer__pb2.Path.SerializeToString,
            nfsServer__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NFSServer/MoveDirectory',
            nfsServer__pb2.SourceDestinationPath.SerializeToString,
            nfsServer__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CopyDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NFSServer/CopyDirectory',
            nfsServer__pb2.SourceDestinationPath.SerializeToString,
            nfsServer__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RenameDirectory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NFSServer/RenameDirectory',
            nfsServer__pb2.SourceDestinationPath.SerializeToString,
            nfsServer__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
