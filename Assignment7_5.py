import threading

def Display(No):
    print("\nNumbers 1 to 50: ")
    for i in range(1,No+1):
        print(i, end = " ")

def DisplayReverse(No):
    print("\nNumbers 50 to 1 : ")
    for i in range(No,0,-1):
        print(i, end=" ")


def main():
    print("Demonstration of parallel programming.")
    Number = 50

    thread1 = threading.Thread(target = Display, args = (Number,))
    thread2 = threading.Thread(target = DisplayReverse, args=(Number,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()