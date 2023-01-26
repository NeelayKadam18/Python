from sys import *
from os import *

def Script_Task(No):
    if((No % 2) == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("---------------Automations--------------------")
    print("Automation Script started with name : ",argv[0])
    
    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()
        
    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is used to perform __________")
        exit()

    elif((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ________ number of arguments as")
        print("First Argument as : ___________")
        print("Second Argument as : ___________")
        exit()
        
    else:
        Script_Task(int(argv[1]))
        #print("There is no such option in the script as : ",argv[1])
        #exit()

if __name__ == "__main__":
    main()