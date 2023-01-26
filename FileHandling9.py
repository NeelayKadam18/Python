import os

def WordSearch(FileName, Word):
    try:
        fd = open(FileName, "r")
        Data = fd.read()
        String = Data.split()

        counter = 0
        for i in String:
            if (i == Word):
                counter = counter + 1

        print("The word '{}' occured {} times".format(Word,counter))

        fd.close()

    except:
        print("File doesn't exists.")


def main():
    print("Enter the file name: ")
    Name = input()

    print("Enter the word to search from file :")
    Word = input()

    WordSearch(Name,Word)
    
if __name__ == "__main__":
    main()