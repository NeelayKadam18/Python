# File Handling
import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if(size == 0):
            os.remove(FileName)
        else:
            print("Are yous sure to delete the file? Y/N")
            option = input()
            if(option == "Y" or option == "y"):
                os.remove(FileName)
            else:
                print("File deletion process stopped.")
    else:
        print("File doesn't exits.")

def main():
    print("Enter the file name to delete: ")
    Name = input()

    DeleteFile(Name)
    
if __name__ == "__main__":
    main()