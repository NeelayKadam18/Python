import threading

def EvenList(NumberList):

    Sum = 0
    for i in NumberList:
        if(i % 2 == 0):
            print("Even Number from list: ", i)
            Sum = Sum + i

    print("Addition of Even Numbers : ",Sum)


def OddList(NumberList):
    
    Sum = 0
    for i in NumberList:
        if ((i % 2) != 0):
            print("Odd Number from list : ", i)
            Sum = Sum + i


    print("Addition of Odd Numbers : ", Sum)


def main():
    
    print("Demonstration of parallel programming.")
    print("Enter how many elements you want in the list: ")
    No = int(input())
    NumberList = []
    print("Enter numbers in the list: ")
    for i in range(No):
        Value = int(input())
        NumberList.append(Value)

    evenlist = threading.Thread(target = EvenList, args = (NumberList,))
    oddlist = threading.Thread(target = OddList, args=(NumberList,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()


if __name__ == "__main__":
    main()