
print("Application to add the digits of a given integer.")

def Length(Value):
    sum = 0
    for i in str(Value):
        sum = sum + int(i)
    return sum

def main():
    print("Enter a number: ")
    no1= int(input())
    length = Length(no1)
    print("Addition of digits is: ",length)
        
if __name__ == "__main__":
    main()