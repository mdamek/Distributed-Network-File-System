# Distributed-Network-File-System

Implementation of Distributed Network File System from scratch. 
Server select folder on machine and provide actions for it to clients.
To communicate and remote procedure calls it use gRPC.

## Avaliable commands

- ls - list all folders and files in folder
- cd <name of folder> or <..> - go to selected folder/go higher
- exit - exit program
- mkdir <directory name> - create directory in actual directory
- rmdir <directory name> - delete directory in actual directory
- cpdir <total path of source directory> <total path of destination directory> - copy directory
- mvdir <total path of source directory> <total path of destination directory> - move directory
- rendir <total path of source directory> <total path of destination directory> - rename directory
- ren <total path of source file> <total path of destination file> - rename file
- mv <total path of source file> <total path of destination file> - move file
- cp <total path of source file> <total path of destination file> - copy file
- rm <file name> - remove file from actual directory
- read <file name> - show content of selected file from actual directory
- write <file name> - create new file/append text to existing/override file from actual directory

## Usage

1. go to folder NFS
2. Install requirements.txt
3. run: python server.py
4. Run: python client.py

