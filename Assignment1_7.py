print("Application to check the number's divisibility by 5 ")

def DivideByFxive(Value):
    if(Value%5==0):
        return True
    else:
        return False

def main():
    print("\nEnter the number : ")
    no1 = input()

    Value = DivideByFive(int(no1))
    print(Value)

if __name__ == "__main__":
    main()