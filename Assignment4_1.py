
print("Application to demonstrate lambda function to return number's power of two.\n")

Power = lambda A : A**2

def main():
    print("Enter a number : ")
    no1= int(input())

    power = Power(no1)
    print("Power of two is : ",power)

if __name__ == "__main__":
    main()