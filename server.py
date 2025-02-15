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
        print("List directory: ", path)
        folders = []
        files = []
        for (dirpath, dirnames, filenames) in walk(path):
            folders.extend(dirnames)
            files.extend(filenames)
            break
        return nfsServer_pb2.FolderContents(path = os.path.abspath(path), folders = json.dumps(folders), files = json.dumps(files))

    # directories operations

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

    # files operations

    def DeleteFile(self, request, context):
        def fun():
            path = request.path
            os.remove(path)
            print("Remove file: ", path)
        return self.HandleCommandAndException(fun)

    def CopyFile(self, request, context):
        print(request)
        def fun():
            source = request.source
            destination = request.destination
            shutil.copy2(source, destination)
            print("Copy file from: ", source, " to: ", destination)
        return self.HandleCommandAndException(fun)
        
    def MoveFile(self, request, context):
        def fun():
            source = request.source
            destination = request.destination
            shutil.move(source, destination)
            print("Copy file from: ", source, " to: ", destination)
        return self.HandleCommandAndException(fun)

    def RenameFile(self, request, context):
        def fun():
            source = request.source
            destination = request.destination
            os.rename(source, destination)
            print("Rename file from: ", source, " to: ", destination)
        return self.HandleCommandAndException(fun)

    def ReadFile(self, request, context):
        path = request.path
        with open(path, "rb") as f:
            data = f.read()
        print("Read file: ", path)
        return nfsServer_pb2.File(path = path, content = data)
    
    def EditFile(self, request, context):
        print("Im here")
        def fun():
            path = request.path
            content = request.content
            override = request.override
            print("Edit file: ", path, "override? ", override)
            if override: 
                f = open(path, "w")
            else:
                f = open(path, "a")
            f.write(content.decode("utf-8"))
            f.close()
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