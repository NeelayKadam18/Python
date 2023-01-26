
print("Application to demonstrate object oriented programming.\n")

class Circle:
    
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter radius of circle : ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Radius of Circle is : ", self.Radius)
        print("Area of Circle is : ", self.Area)
        print("Circumference of Circle is : ", self.Circumference)

def main():
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()