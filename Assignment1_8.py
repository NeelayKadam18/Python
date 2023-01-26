print("Application to accept a number and print that many * on console.")

def main():
    print("\nEnter the number : ")
    no1 = int(input())
    print()

    i=0
    while(i<no1):
        print("*",end=" ")
        i=i+1

if __name__ == "__main__":
    main()