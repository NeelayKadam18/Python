# Head Recursion Example

def Display(No):
    if(No > 0):
        Display(No-1)
        print(No, end=" ")

def main():
    Display(5)

if __name__ == "__main__":
    main()
