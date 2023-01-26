CheckEven = lambda No: (No%2 ==0)

Mult = lambda No: No*2

Sum = lambda A,B: A+B

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
    
def reduceX(Helper_Function,Data):
    Sum = 0
    for i in Data:
        Sum =  Helper_Function(i,Sum)
    return Sum

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

    Data_Reduce = reduceX(Sum,Data_Map)

    print("Data after reduce is : ",Data_Reduce)
    
if __name__ == "__main__":
    main()
