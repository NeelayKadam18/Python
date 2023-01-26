# Sum of Digits

def SumOfDigit(No):
    if (No == 0):
        return 0
    else:
        div = int(No/10)
        No = No % 10 + SumOfDigit(div)
        return No
def main():
    Sum = SumOfDigit(879)
    print("Sum of digits is : ",Sum)
if __name__ == "__main__":
    main()
