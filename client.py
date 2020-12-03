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
        pass
    if command == "rmdir":
        pass
    if command == "cpdir":
        pass
    if command == "mvdir":
        pass
    if command == "rendir":
        pass
    
path = nfsServer_pb2.Path(path = "")
result = stub.ListDirectory(path)
rootPath = result.path
actualPath = result.path
actualFiles = json.loads(result.files)
actualFolders = json.loads(result.folders)
printAllFolder(convertConcatListOfFilesAndFolders(result.folders, result.files))

avaliableCommands = ["ls", "cd", "mkdir", "rmdir", "cpdir", "mvdir", "rendir"]

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
    
    