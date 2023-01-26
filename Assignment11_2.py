import os
from sys import *
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirname, subdirs, filelist in os.walk(path):
            for filen in filelist:
                path = os.path.join(dirname, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates found")
        if (os.path.exists("Log.txt")):
            print("File Already Exists.")
        else:
            fd = open("Log.txt", "w")
        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    fd.write(subresult)
                    fd.write("\n")
                    fd.close
            icnt = 0
    else:
        print("No Duplicates Found")

def main():
    print("Directory Watcher Application")

    if(len(argv) != 2):
        print("Insufficient Arguments")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("This script will traverse the specific directory and remove the duplicate files.")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Application_name AbsolutePath_Of_Directory")
        exit()

    try:
        
        arr= FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of Input.")

    except Exception as E:
        print("Error : Invalid Input : ",E)

if __name__ == "__main__":
    main()