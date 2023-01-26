
print("Application to accept 'n' numbers, store it in list and add all prime numbers from the list: \n")
import MarvellousNum

def ListPrime(list):
    primeList = []
    Sum = 0

    for i in list:
        Value = MarvellousNum.ChkPrime(i)
        if(Value != None):
            primeList.append(Value)

    for Value in primeList:
        Sum = Sum + Value

    return Sum

def main():
    print("Enter the number of elements : ")
    no1= int(input())

    numberList = []
        
    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    primeSum = ListPrime(numberList)

    print("Sum of prime numbers is : ",primeSum)
        
if __name__ == "__main__":
    main()