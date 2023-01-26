print("Application to print whether the number is positive, negative or zero.")

def CheckNum(Value):
    if(Value>0):
        return 1
    elif(Value<0):
        return 2
    else:
        return 0

def main():
    print("\nEnter the number : ")
    no1 = input()

    Value = CheckNum(int(no1))

    if (Value == 1):
        print("Positive Number.")
    elif(Value == 2):
        print("Negative Number.")
    else:
        print("Zero.")

if __name__ == "__main__":
    main()