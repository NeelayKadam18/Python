print("Application to find whether the number is Even or Odd. ")

def ChkNum(Value):
    if(Value%2==0):
        return 1
    else:
        return 0

def main():
    print("\nEnter the number : ")
    no1 = input()
    
    Value = ChkNum(int(no1))

    if(Value==1):
        print("Even Number.")
    else:
        print("Odd Number.")

if __name__ == "__main__":
    main()