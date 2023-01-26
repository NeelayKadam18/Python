
print("Application to demonstrate factorial of a number.")

def FactorSum(No):
    i = 1
    Value = 0
    while (i <= int(No / 2)):
        if (No % i == 0):
            Value = Value + i
        i = i + 1
    return Value

def main():
    print("Enter a number: ")
    no1= int(input())

    Fact =  FactorSum(no1)
    print("Sum of factors is : ",Fact)
        
if __name__ == "__main__":
    main()