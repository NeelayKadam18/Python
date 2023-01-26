print("Application to demonstrate function arguments.")

def Add(*Values):
    #print(type(Values))
    #print("Number of Arguments are : ",len(Values))
    sum = 0
    for i in Values:
        sum = sum + i
    return sum

def AddX(*Values):
    #print(type(Values))
    #print("Number of Arguments are : ",len(Values))
    sum = 0
    for i in range(len(Values)):
        sum = sum + Values[i]
    return sum

def main():
    Ans = Add(10,11)
    print("Addition is : ",Ans)

    Ans = Add(10, 10, 10, 10)
    print("Addition is : ", Ans)

    Ans = AddX(10, 10, 10)
    print("Addition is : ", Ans)

if __name__ == "__main__":
    main()