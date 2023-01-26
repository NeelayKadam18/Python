
print("Application to demonstrate Filter, Map and Reduce.\n")

def checkPrime(Value):
    if Value > 1:
        for i in range(2, int(Value / 2) + 1):
            if ((Value % i) == 0):
                break
        else:
            return True
    

def multiply(number):
    return number*2

def Max(A,B):
    if (A>B):
        return A
    else:
        return B

def filterX(function,data):
    arr = []
    for Value in data:
        if(function(Value) == True):
            arr.append(Value)

    return arr

def mapX(function,data):
    arr = []
    for i in data:
        Value = function(i)
        arr.append(Value)

    return arr

def reduceX(function,data):
    Max = data[0]
    for i in data:
        if (Max < function(Max,i)):
            Max = function(Max,i)
    return Max

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    data_filter = filterX(checkPrime,numberList)
    print("Data after filter : ",data_filter)

    data_map = mapX(multiply, data_filter)
    print("Data after map : ", data_map)

    data_reduce = reduceX(Max, data_map)
    print("Data after reduce : ", data_reduce)
        
if __name__ == "__main__":
    main()