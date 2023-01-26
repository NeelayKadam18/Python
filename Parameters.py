print("Application to demonstrate function arguments.")

# Positional argument / Keyword Argument
def Add1(No1,No2):
    print("Value of No1 : ",No1)
    print("Value of No2 : ", No2)
    return No1+No2

def main():
    Ans = 0
    Ans = Add1(11,10)
    print("Addition is : ",Ans)

    Ans = Add1(No2= 11,No1= 10)
    print("Addition is : ", Ans)

    Ans = Add1(No1=11, No2=10)
    print("Addition is : ", Ans)

if __name__ == "__main__":
    main()