import threading

def EvenFactors(No):

    Sum = 0
    for i in range(1,No):
        if(i % 2 == 0):
            if (No % i == 0):
                print("Even Factor is : ", i)
                Sum = Sum + i

    print("Addition of Even Factors : ",Sum)


def OddFactors(No):
    
    Sum = 0
    for i in range(1, No):
        if ((i % 2) != 0):
            if (No % i == 0):
                print("Odd Factor is : ", i)
                Sum = Sum + i

    print("Addition of Odd Factors : ", Sum)


def main():
    print("Demonstration of parallel programming.")
    print("Enter the number : ")
    Number = int(input())

    evenfactor = threading.Thread(target = EvenFactors, args = (Number,))
    oddfactor = threading.Thread(target = OddFactors, args=(Number,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()