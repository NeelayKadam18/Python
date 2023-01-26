# File Handling
import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
    else:
        print("File doesn't exits.")

def main():
    print("Enter the file name to delete: ")
    Name = input()

    DeleteFile(Name)
    
if __name__ == "__main__":
    main()