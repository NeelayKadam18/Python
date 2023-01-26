
print("Application to accept n numbers, store it in list and find the minimum.\n")

def Minimum(list):
    Min = list[0]
    for i in list:
        if(i < Min):
            Min = i
    return Min

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    Min = Minimum(numberList)
    print("Minimum of elements in the list is: ",Min)
        
if __name__ == "__main__":
    main()