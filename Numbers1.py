# My Program

class Arithmetic:

    def __init__(self,A):
        print("Inside init method")
        self.l1 = A

    def Addition(self):
        Sum = 0
        for i in self.l1:
            Sum = Sum + i

        return Sum

def main():
    print("How many numbers do you want : ")
    No = int(input())

    list1 = []
    print("Enter the nubers: ")
    for i in range(No):
        Value = int(input())
        list1.append(Value)

    obj = Arithmetic(list1)
    Ans = obj.Addition()
    print("Addition of numbers in list : ",Ans)

if __name__ == "__main__":
    print("Inside starter")
    main()