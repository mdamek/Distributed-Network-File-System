import grpc
from concurrent import futures
import time

import nfsServer_pb2
import nfsServer_pb2_grpc
from os import walk
from pathlib import Path
import json
import shutil
import os


class NFSServicer(nfsServer_pb2_grpc.NFSServer):

    def HandleCommandAndException(self, functionToRun):
        ex = ""
        try:
            functionToRun()
        except Exception as e:
            ex = str(e)
            print("Exception: ", ex)
        return nfsServer_pb2.Result(ex = ex)

    def ListDirectory(self, request, context):
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
        return nfsServer_pb2.FolderContents(path = os.path.abspath(path), folders = json.dumps(folders), files = json.dumps(files))

    def DeleteDirectory(self, request, context):
        def fun():
            path = request.path
            shutil.rmtree(path, ignore_errors=True)
            print("Delete directory: ", path)
        return self.HandleCommandAndException(fun)

    def CreateDirectory(self, request, context):
        def fun():
            path = request.path
            os.mkdir(path)
            print("Create directory: ", path)
        return self.HandleCommandAndException(fun)

    def MoveDirectory(self, request, context):
        print(request)
        def fun():
            source = request.source
            destination = request.destination
            shutil.move(source, destination)
            print("Move directory from: ", source, " to: ", destination)
        return self.HandleCommandAndException(fun)
        
    def CopyDirectory(self, request, context):
        def fun():
            source = request.source
            destination = request.destination
            shutil.rmtree(destination)
            shutil.copytree(source, destination)
            print("Copy directory from: ", source, " to: ", destination)
        return self.HandleCommandAndException(fun)

    def RenameDirectory(self, request, context):
        def fun():
            source = request.source
            destination = request.destination
            os.rename(source, destination)
            print("Rename directory from: ", source, " to: ", destination)
        return self.HandleCommandAndException(fun)

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