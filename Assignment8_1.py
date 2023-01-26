# Print * using recursion

def Display(No):
    if(No > 0):
        No = No - 1
        Display(No)
        print("*",end = " ")

def main():
    Display(5)

if __name__ == "__main__":
    main()
