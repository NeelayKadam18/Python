# Accept two numbers and perform addition and subtraction of it

# What to do? -> Behaviour (Function) -> Addition and Subtraction
# What we need to do that? -> Characteristics (Data) -> 2 numbers

# Class = Characteristics + Behaviour
# Class = Data + Functions

# First Class object

class Arithmetic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1 + self.No2

    def Sub(self):
        return self.No1 - self.No2


def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    obj = Arithmetic(Value1,Value2)
    
    Ans = obj.Add()
    print("Addition is : ",Ans)

    Ans = obj.Sub()
    print("Subtraction is : ",Ans)

          
if __name__ == "__main__":
    main()
