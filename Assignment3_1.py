
print("Application to accept n numbers, store it in list and add all the numbers.\n")

def Addition(list):
    Sum = 0
    for i in list:
        Sum = Sum + i

    return Sum

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    Sum = Addition(numberList)
    print("Addition of elements in the list is: ",Sum)
        
if __name__ == "__main__":
    main()