# File Handling

def CreateFile(FileName):
    fd = open(FileName,"w")                # open() used to create as well as open the file

def main():
    print("Enter the file name to create: ")
    Name = input()

    CreateFile(Name)
    
if __name__ == "__main__":
    main()