
print("Application to demonstrate factorial of a number.")

def Fact(Value1):
    i=Value1
    while(i>1):
        a = Value1*(i-1)
        Value1 = a
        i = i-1
    return Value1


def main():
    print("Enter a number: ")
    no1= int(input())
    
    Factorial = Fact(no1)
    print("Factorial is: ",Factorial)
        
if __name__ == "__main__":
    main()