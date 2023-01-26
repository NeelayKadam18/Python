def CheckEven(No):
    return (No%2 ==0)

def Mult(No):
    return No*2

def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if(Helper_Function(No)==True):
            Result.append(No)
    return Result

def mapX(Helper_Function,Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)
        Result.append(Value)
    return Result
    

def main():
    print("Enter number of elements you want to enter: ")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data: ")
    for iCnt in range(iSize):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)

    Data_Filter = filterX(CheckEven,Data_Input)

    print("Data after filter is : ",Data_Filter)

    Data_Map = mapX(Mult,Data_Filter)

    print("Data after map is : ",Data_Map)

    
if __name__ == "__main__":
    main()
