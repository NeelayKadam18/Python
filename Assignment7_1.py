import threading

def DisplayEven(No):
    for i in range(1,No):
        if(i % 2 == 0):
            print("Even Number : ", i)

def DisplayOdd(No):
    for i in range(1,No):
        if(i % 2 != 0):
            print("Odd Number : ", i)

def main():
    print("Demonstration of parallel programming.")
    Number = 20

    p1 = threading.Thread(target = DisplayEven, args = (Number,))
    p2 = threading.Thread(target = DisplayOdd, args=(Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()