
class Numbers:

    def __init__(self):
        self.Size = 0
        self.Arr = list()
        # self.Arr = []

    def Accept(self):
        print("How many numbers do you want : ")
        self.Size = int(input())

        print("Enter the numbers : ")
        Value = 0
        for i in range(self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are: ")
        for i in range(self.Size):
            print(self.Arr[i], end = " ")

    def Addition(self):
        Sum = 0
        for i in self.Arr:
            Sum = Sum + i

        return Sum

    def Average(self):
        Sum = 0
        for i in self.Arr:
            Sum = Sum + i

        return (Sum/self.Size)

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(self.Size):
            if(self.Arr[i] > Max):
                Max = self.Arr[i]

        return Max

    def Minimum(self):
        Min = self.Arr[0]
        for i in range(self.Size):
            if(self.Arr[i] < Min):
                Min = self.Arr[i]

        return Min
    
def main():
    obj = Numbers ()
    obj.Accept()
    obj.Display()

    Ans = obj.Addition()
    print("\nAddition of all elements is : ", Ans)

    Ans = obj.Average()
    print("\nAverage of all elements is : ", Ans)

    Ans = obj.Maximum()
    print("\nMaximum of all elements is : ", Ans)

    Ans = obj.Minimum()
    print("\nMinimum of all elements is : ", Ans)

if __name__ == "__main__":
    print("Inside starter")
    main()