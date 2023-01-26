import os
import filecmp
from sys import *

def FileCompare(File1, File2):
    compare = filecmp.cmp(File1, File2)
    if compare == True:
        print("File contents are same.")
    else:
        print("File contents are different.")


def main():
    if (len(argv) < 3):
        print("Insufficient Arguments.")

    elif (argv[1] == "-h"):
        print("This script will traverse the directory and display the name of all the entries.")
        exit()

    elif (argv[1] == "-u"):
        print("Usage : Application_name FileName1 FileName2")
        exit()

    FileCompare(argv[1],argv[2])

if __name__ == "__main__":
    main()
