
print("Application to find length of a given integer.")

def Length(Value):
    counter = 0
    for i in range(len(Value)):
        counter= counter + 1
    return counter

def main():
    print("Enter a number: ")
    no1= input()
    length = Length(no1)
    print("Length is: ",length)
        
if __name__ == "__main__":
    main()