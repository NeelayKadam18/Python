
class Arithmetic:

    def __init__(self):
        self.Size = 0
        self.Arr = list()
        # self.Arr = []

    def Accept(self):
        print("How many numbers do you want : ")
        self.Size = int(input())

        print("Enter the nubers: ")
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
    
def main():
    obj = Arithmetic()
    obj.Accept()
    obj.Display()

    Ans = obj.Addition()
    print("\nAddition is : ", Ans)

    Ans = obj.Average()
    print("\nAverage is : ", Ans)

if __name__ == "__main__":
    print("Inside starter")
    main()