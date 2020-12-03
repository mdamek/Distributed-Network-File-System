import grpc
import tkinter as tk
import nfsServer_pb2
import nfsServer_pb2_grpc
import json

channel = grpc.insecure_channel('localhost:50051')
stub = nfsServer_pb2_grpc.NFSServerStub(channel)

global rootPath
global actualPath
global actualFolders
global actualFiles

rootPath = ""
actualPath = ""
actualFolders = []
actualFiles = []

def convertConcatListOfFilesAndFolders(folders, files):
    folders = json.loads(folders)
    files = json.loads(files)
    return folders + files

def printAllFolder(allFromDirectory):
    for item in allFromDirectory:
        if item in actualFiles:
            item = "*" + item
        print(item)

def takeOnlyCommand(allCommand):
    return allCommand.split(" ")[0]

def useRemoteFunction(allCommand):
    command = takeOnlyCommand(allCommand)
    seperatedArguments = allCommand.split(" ")
    global actualPath
    global actualFiles
    global actualFolders
    global rootPath
    if command == "ls":
        path = nfsServer_pb2.Path(path = actualPath)
        result = stub.ListDirectory(path)
        actualPath = result.path
        printAllFolder(convertConcatListOfFilesAndFolders(result.folders, result.files))
    if command == "cd":
        if seperatedArguments[1] in actualFolders or seperatedArguments[1] == "..":
            if seperatedArguments[1] is "..":
                regularPath = actualPath + "\\.."
            else:
                regularPath = actualPath + "\\" + seperatedArguments[1]
            if regularPath == rootPath + "\\..":
                print("Access denied")
                return
            path = nfsServer_pb2.Path(path = regularPath)
            result = stub.ListDirectory(path)
            actualPath = result.path
            actualFiles = json.loads(result.files)
            actualFolders = json.loads(result.folders)
            printAllFolder(convertConcatListOfFilesAndFolders(result.folders, result.files))
            return
        else:
            print("Wrong folder")
        
    if command == "mkdir":
        if seperatedArguments[1] in actualFolders:
            print("Folder already exist")
            return
        path = nfsServer_pb2.Path(path = actualPath + "\\" + seperatedArguments[1])
        result = stub.CreateDirectory(path)
        if(result.ex != ""):
            print (result.ex)
    if command == "rmdir":
        if seperatedArguments[1] not in actualFolders:
            print("Folder not exist")
            return
        path = nfsServer_pb2.Path(path = actualPath + "\\" + seperatedArguments[1])
        result = stub.DeleteDirectory(path)
        if(result.ex != ""):
            print (result.ex)
    if command == "cpdir":
        paths = nfsServer_pb2.SourceDestinationPath(source = seperatedArguments[1], destination = seperatedArguments[2])
        result = stub.CopyDirectory(paths)
        if(result.ex != ""):
            print (result.ex)
    if command == "mvdir":
        paths = nfsServer_pb2.SourceDestinationPath(source = seperatedArguments[1], destination = seperatedArguments[2])
        result = stub.MoveDirectory(paths)
        if(result.ex != ""):
            print (result.ex)
    if command == "rendir":
        paths = nfsServer_pb2.SourceDestinationPath(source = seperatedArguments[1], destination = seperatedArguments[2])
        result = stub.RenameDirectory(paths)
        if(result.ex != ""):
            print (result.ex)
    if command == "ren":
        paths = nfsServer_pb2.SourceDestinationPath(source = seperatedArguments[1], destination = seperatedArguments[2])
        result = stub.RenameFile(paths)
        if(result.ex != ""):
            print (result.ex)
    if command == "mv":
        paths = nfsServer_pb2.SourceDestinationPath(source = seperatedArguments[1], destination = seperatedArguments[2])
        result = stub.MoveFile(paths)
        if(result.ex != ""):
            print (result.ex)
    if command == "cp":
        paths = nfsServer_pb2.SourceDestinationPath(source = seperatedArguments[1], destination = seperatedArguments[2])
        result = stub.CopyFile(paths)
        if(result.ex != ""):
            print (result.ex)
    if command == "rm":
        if seperatedArguments[1] not in actualFiles:
            print("File not exist")
            return
        path = nfsServer_pb2.Path(path = actualPath + "\\" + seperatedArguments[1])
        result = stub.DeleteFile(path)
        if(result.ex != ""):
            print (result.ex)
    
path = nfsServer_pb2.Path(path = "")
result = stub.ListDirectory(path)
rootPath = result.path
actualPath = result.path
actualFiles = json.loads(result.files)
actualFolders = json.loads(result.folders)
printAllFolder(convertConcatListOfFilesAndFolders(result.folders, result.files))

avaliableCommands = ["ls", "cd", "mkdir", "rmdir", "cpdir", "mvdir", "rendir", "ren", "mv", "cp", "rm"]

while(True):
    print("\nActual remote path: ", actualPath)
    print("You can use: ls, cd, mkdir, rmdir...")
    allCommand = input()
    print()
    command = takeOnlyCommand(allCommand)
    if command not in avaliableCommands:
        print("Invalid command. Try again")
        continue
    useRemoteFunction(allCommand)
    
    