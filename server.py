import grpc
from concurrent import futures
import time

import nfsServer_pb2
import nfsServer_pb2_grpc
from os import walk
from pathlib import Path
import json


class NFSServicer(nfsServer_pb2_grpc.NFSServer):

    def ListDir(self, request, context):
        print("WEAREAD")
        path = request.path
        if not path:
            path = str(Path.home())
        print("Used path: ", path)
        folders = []
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            folders.extend(dirnames)
            files.extend(filenames)
            break
        return nfsServer_pb2.FolderContents(path = path, folders = json.dumps(folders), files = json.dumps(files))


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
nfsServer_pb2_grpc.add_NFSServerServicer_to_server(
        NFSServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)