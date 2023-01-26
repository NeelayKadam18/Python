import threading

def smallLetter(string):
    for char in string:
        if (char.islower()):
            print("Small Letter : ",char)

def capitalLetter(string):
    for char in string:
        if(char.isupper()):
            print("Capital Letter : ",char)

def digitE(string):
    for char in string:
        if (char.isdigit()):
            print("Digit : ",char)

def main():
    
    print("Demonstration of parallel programming.")
    print("Enter a string: ")
    string = input()

    small = threading.Thread(target = smallLetter, args = (string,))
    capital = threading.Thread(target = capitalLetter, args=(string,))
    digit = threading.Thread(target = digitE, args=(string,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()


if __name__ == "__main__":
    main()