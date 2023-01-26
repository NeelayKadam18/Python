print("Application to print the length of the string.")

def FindLength(Value):
    return len(Value)

def main():
    print("Enter the String: ")
    string = input()

    Value = FindLength(string)
    print(Value)

if __name__ == "__main__":
    main()