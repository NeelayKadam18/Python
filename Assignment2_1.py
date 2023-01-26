from Arithmetic import *

print("Application to demonstrate Addition, Subtraction, Multiplication and Division of two numbers.")

def main():
    print("\nEnter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    Sum = Add(no1,no2)
    print("Addition is : ", Sum)

    Subtract = Sub(no1, no2)
    print("Subtraction is : ", Subtract)

    Multiply = Mult(no1, no2)
    print("Multiplication is : ", Multiply)

    Divide = Div(no1, no2)
    if (Divide == False):
        print("Division by 0 not possible.")
    else:
        print("Division is : ", Divide)

if __name__ == "__main__":
    main()