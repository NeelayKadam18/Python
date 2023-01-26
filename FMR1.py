print("Application to demonstrate Filter Map Reduce\n")

def CheckEven(No):
    return (No%2 ==0)

def Increment(No):
    return No+2

def Add(A,B):
    return A+B

def filterX(Arr,Function_Name):
    Result = []
    for no in Arr:
        if(Function_Name(no)):
            Result.append(no)
    return Result

def mapX(Arr,Function_Name):
    Result = []
    for no in Arr:
        value = Function_Name(no)
        Result.append(value)
    return Result

def reduceX(Arr,Function_Name):
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    return Sum

def main():
    Data = [12, 3, 1, 6, 4, 5]
    print("Original Data : ",Data)
    Data_Filter = list(filterX(Data,CheckEven))
    print("Data after filter : ",Data_Filter)
    Data_Map = list(mapX(Data_Filter,Increment))
    print("Data after Map : ",Data_Map)
    Ret = reduceX(Data_Map,Add)
    print("Data after reduce : ",Ret)

if __name__=="__main__":
    main()


