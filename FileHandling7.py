import os
from sys import *
import shutil

def CopyFile(FileName):
    shutil.copyfile("Demo.txt", FileName)
    print("Contents of Demo.txt copied into file {} successfully".format(FileName))

def CreateFile(FileName):
    if (os.path.exists(FileName)):
        print("File Already Exists.")
    else:
        fd = open(FileName, "w")
        print("File Created Successfully")
        CopyFile(FileName)

def main():
    if (len(argv) < 2):
        print("Insufficient Arguments")
        exit()

    if (argv[1] == "-h"):
        print("This script will traverse the directory and display the name of all the entries.")
        exit()

    if (argv[1] == "-u"):
        print("Usage : Application_name File_name")
        exit()

    CreateFile(argv[1])


if __name__ == "__main__":
    main()