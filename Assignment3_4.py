
print("Application to accept n numbers, store it in list and find the frequency of a particular element from the list.\n")

def Frequency(list, number):
    counter = 0

    for i in list:
        if(i == number):
            counter+= 1

    return counter

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    print("Enter number to search in the list : ")
    numberToSearch = int(input())

    freq = Frequency(numberList, numberToSearch)
    print("Frequency of the element is: ",freq)
        
if __name__ == "__main__":
    main()