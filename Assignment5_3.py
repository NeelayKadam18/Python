
print("Application to demonstrate object oriented programming.\n")

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first Value : ")
        self.Value1 = int(input())

        print("Enter second Value : ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Subraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if(self.Value2 == 0):
            print("Division by 0 is not possible.")
        else:
            return self.Value1/self.Value2

def main():
    obj1 = Arithmetic()
 
    obj1.Accept()

    Add = obj1.Addition()
    print("Addition is : ",Add)

    Sub = obj1.Subraction()
    print("Subtraction is : ",Sub)

    Mult  = obj1.Multiplication()
    print("Multiplication is : ",Mult)

    Div = obj1.Division()
    print("Division is : ",Div)


if __name__ == "__main__":
    main()