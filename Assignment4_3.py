
print("Application to demonstrate Filter, Map and Reduce.\n")

def betweenNumber(number):
    return (number>=70 and number<=90)
    

def increment(number):
    return number+10

def multiplication(A,B):
    return A*B

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
    product = 1
    for i in data:
        product = multiplication(product,i)

    return product

def main():
    print("Enter the number of elements : ")
    no1= int(input())
    numberList = []

    print("Enter the elements : ")
    for i in range(no1):
        value = int(input())
        numberList.append(value)

    data_filter = filterX(betweenNumber,numberList)
    print("Data after filter : ",data_filter)

    data_map = mapX(increment, data_filter)
    print("Data after map : ", data_map)

    data_reduce = reduceX(multiplication, data_map)
    print("Data after reduce : ", data_reduce)
        
if __name__ == "__main__":
    main()