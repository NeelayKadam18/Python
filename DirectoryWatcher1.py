import os
from sys import *

# Automate the boring stuff in python - Book
# os.walk() -> search python.org

# python DirectoryWatcher.py D:\Python\13-11-2022\A      -> Absolute path
# python DirectoryWatcher.py A                           -> Relative path
# windows join linux join are different i.e / or \
# getcwd() -> get current working directory
# size on disk(Total -> 1kb, 2kb, 4kb or 8kb) --------- actual file size(getsize()->used size)

# checksum -> exact replica files  -> DirectoryCleaner -> LogFile -> Scheduling -> Mail Log

def Directory_Watcher(Dir_Name):
    print("Inside directory watcher method")
    print("Name of input directory : ",Dir_Name)

    flag = os.path.isabs(Dir_Name)
    if(flag == False):
        Dir_Name = os.path.abspath(Dir_Name)

    exists = os.path.isdir(Dir_Name)

    if exists:
        for foldername, subfolder, filenames in os.walk(Dir_Name):
            print("Folder Name is : ",foldername)
            print("having size ", os.path.getsize(foldername))

            for subf in subfolder:                                      # Optional loop
                print("Subfolder Name of "+foldername+" is "+subf)

            for fnames in filenames:
                print("File inside folder "+foldername+" is "+fnames)
                print("having size ",os.path.getsize(os.path.join(foldername,fnames)))     # complete till the path to getsize() join particular folder with the file

            print(" ")

    else:
        print("Invalid path")

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