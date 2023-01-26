import os
from sys import *

# Automate the boring stuff in python - Book
# os.walk() -> search python.org

# python DirectoryWatcher.py D:\Python\13-11-2022\A      -> Absolute path
# python DirectoryWatcher.py A                           -> Relative path

def Directory_Watcher(Dir_Name):
    print("Inside directory watcher method")
    print("Name of input directory : ",Dir_Name)

    for foldername, subfolder, filenames in os.walk(Dir_Name):
        print("Folder Name is : ",foldername)

        for subf in subfolder:                                      # Optional loop
            print("Subfolder Name of "+foldername+" is "+subf)

        for fnames in filenames:
            print("File inside folder "+foldername+" is "+fnames)
            
        print(" ")

def main():
    print("Directory Watcher Application")

    if(len(argv) < 2):
        print("Insufficient Arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will traverse the directory and display the name of all the entries.")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Directory_name")
        exit()

    Directory_Watcher(argv[1])

if __name__ == "__main__":
    main()