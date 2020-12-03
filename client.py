import grpc

# import the generated classes
import nfsServer_pb2
import nfsServer_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = nfsServer_pb2_grpc.NFSServerStub(channel)

# create a valid request message
path = nfsServer_pb2.Path(path = "")
# make the call
response = stub.ListDir(path)

print(response)