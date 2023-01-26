import time

def DisplayEven(No):
    for i in range(1,No):
        if(i % 2 == 0):
            print("Even Number : ", i)

def DisplayOdd(No):
    for i in range(1,No):
        if(i % 2 != 0):
            print("Odd Number : ", i)

def main():
    print("Demonstration of Serial Programming")
    DisplayEven(2000)
    DisplayOdd(2000)
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Execution time is : ",end_time-start_time)
    # Execution time = 0.643 (Whole execution time of Application)