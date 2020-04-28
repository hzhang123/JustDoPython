# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import segmentation_pb2 as segmentation__pb2


class SegServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSegCountByProjects = channel.unary_unary(
                '/io.growing.segmentation.grpc.v1.SegService/GetSegCountByProjects',
                request_serializer=segmentation__pb2.SegCountRequest.SerializeToString,
                response_deserializer=segmentation__pb2.SegCountReply.FromString,
                )
        self.BatchCreateSeg = channel.unary_unary(
                '/io.growing.segmentation.grpc.v1.SegService/BatchCreateSeg',
                request_serializer=segmentation__pb2.BatchCreateSegRequest.SerializeToString,
                response_deserializer=segmentation__pb2.BatchSegReply.FromString,
                )
        self.BatchUpdateSegId = channel.unary_unary(
                '/io.growing.segmentation.grpc.v1.SegService/BatchUpdateSegId',
                request_serializer=segmentation__pb2.BatchUpdateSegIdRequest.SerializeToString,
                response_deserializer=segmentation__pb2.BatchSegReply.FromString,
                )
        self.CreateSegmentExportJob = channel.unary_unary(
                '/io.growing.segmentation.grpc.v1.SegService/CreateSegmentExportJob',
                request_serializer=segmentation__pb2.CreateSegmentExportJobRequest.SerializeToString,
                response_deserializer=segmentation__pb2.CreateSegmentExportJobReply.FromString,
                )


class SegServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetSegCountByProjects(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateSeg(self, request, context):
        """rpc GetSegsProject(SegRequest) returns (SegReply) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchUpdateSegId(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSegmentExportJob(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SegServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSegCountByProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSegCountByProjects,
                    request_deserializer=segmentation__pb2.SegCountRequest.FromString,
                    response_serializer=segmentation__pb2.SegCountReply.SerializeToString,
            ),
            'BatchCreateSeg': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchCreateSeg,
                    request_deserializer=segmentation__pb2.BatchCreateSegRequest.FromString,
                    response_serializer=segmentation__pb2.BatchSegReply.SerializeToString,
            ),
            'BatchUpdateSegId': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchUpdateSegId,
                    request_deserializer=segmentation__pb2.BatchUpdateSegIdRequest.FromString,
                    response_serializer=segmentation__pb2.BatchSegReply.SerializeToString,
            ),
            'CreateSegmentExportJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSegmentExportJob,
                    request_deserializer=segmentation__pb2.CreateSegmentExportJobRequest.FromString,
                    response_serializer=segmentation__pb2.CreateSegmentExportJobReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'io.growing.segmentation.grpc.v1.SegService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SegService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetSegCountByProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.growing.segmentation.grpc.v1.SegService/GetSegCountByProjects',
            segmentation__pb2.SegCountRequest.SerializeToString,
            segmentation__pb2.SegCountReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchCreateSeg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.growing.segmentation.grpc.v1.SegService/BatchCreateSeg',
            segmentation__pb2.BatchCreateSegRequest.SerializeToString,
            segmentation__pb2.BatchSegReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchUpdateSegId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.growing.segmentation.grpc.v1.SegService/BatchUpdateSegId',
            segmentation__pb2.BatchUpdateSegIdRequest.SerializeToString,
            segmentation__pb2.BatchSegReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSegmentExportJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/io.growing.segmentation.grpc.v1.SegService/CreateSegmentExportJob',
            segmentation__pb2.CreateSegmentExportJobRequest.SerializeToString,
            segmentation__pb2.CreateSegmentExportJobReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)