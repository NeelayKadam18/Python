
print("Application to demonstrate lambda function to multiply two numbers.\n")

Multiplication = lambda A,B : A*B

def main():
    print("Enter first number : ")
    no1= int(input())

    print("Enter second number : ")
    no2 = int(input())

    mult = Multiplication(no1,no2)
    print("Multiplication is : ",mult)

if __name__ == "__main__":
    main()

    