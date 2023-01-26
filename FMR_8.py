from functools import reduce  # for python 3 we have to import for reduce

#CheckEven = lambda No: (No%2 ==0)

#Mult = lambda No: No*2

#Sum = lambda A,B: A+B

def main():
    print("Enter number of elements you want to enter: ")
    iSize = int(input())
    
    Data_Input = []
    print("Please enter the data: ")
    for iCnt in range(iSize):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is : ",Data_Input)

    #Data_Filter = list(filter(CheckEven,Data_Input))
    Data_Filter = list(filter(lambda No: (No%2 ==0),Data_Input))

    print("Data after filter is : ",Data_Filter)

    #Data_Map = list(map(Mult,Data_Filter))
    Data_Map = list(map(lambda No: No*2,Data_Filter))

    print("Data after map is : ",Data_Map)

    #Data_Reduce = reduce(Sum,Data_Map)
    Data_Reduce = reduce(lambda A,B: A+B,Data_Map)

    print("Data after reduce is : ",Data_Reduce)
    
if __name__ == "__main__":
    main()
