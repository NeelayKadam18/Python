# Tail Recursion Example

def Display(No):
    if(No > 0):
       print(No, end=" ")
       No = No - 1
       Display(No)

def main():
    Display(5)

if __name__ == "__main__":
    main()
