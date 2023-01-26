
print("Application to accept n numbers, store it in list and find the maximum.\n")

def Maximum(list):
    Max = list[0]
    for i in list:
        if(i > Max):
            Max = i
    return Max

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    Max = Maximum(numberList)
    print("Maximum of elements in the list is: ",Max)
        
if __name__ == "__main__":
    main()