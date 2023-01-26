import os

def FileSearch(FileName):
    directory = os.getcwd()
    flag = 0
    for foldername, subfolder, filenames in os.walk(directory):
        for fnames in filenames:
            if(fnames == FileName):
                flag = 1
                dir = foldername
                
    if(flag == 1):
        print("File exists in : ",dir)
    else:
        print("File doesn't exists.")

def main():
    print("Enter the file name to search: ")
    Name = input()

    FileSearch(Name)
    
if __name__ == "__main__":
    main()