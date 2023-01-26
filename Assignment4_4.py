
print("Application to demonstrate Filter, Map and Reduce.\n")

def checkEven(number):
    return (number%2 == 0)
    

def square(number):
    return number**2

def Add(A,B):
    return A+B

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
    Sum = 0
    for i in data:
        Sum = Add(Sum,i)

    return Sum

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    data_filter = filterX(checkEven,numberList)
    print("Data after filter : ",data_filter)

    data_map = mapX(square, data_filter)
    print("Data after map : ", data_map)

    data_reduce = reduceX(Add, data_map)
    print("Data after reduce : ", data_reduce)
        
if __name__ == "__main__":
    main()