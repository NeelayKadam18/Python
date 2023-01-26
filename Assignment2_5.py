
print("Application to find whether number is prime or not.")

def Prime(Value):
    flag = False
    if Value > 1:
        for i in range(2, int(Value/2)+1):
            if (Value % i) == 0:
                flag = True
                break

    if flag:
        return 0
    else:
        return 1

def main():
    print("Enter a number: ")
    no1= int(input())

    prime =  Prime(no1)
    if prime == 1:
        print("It is a prime number")
    else:
        print("It is not a prime number")
        
if __name__ == "__main__":
    main()