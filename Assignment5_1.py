
print("Application to demonstrate object oriented programming.\n")

class Demo:

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("First value is: ",self.no1)

    def Gun(self):
        print("Second value is: ",self.no2)

def main():
    print("Enter first value for object 1: ")
    A = int(input())

    print("Enter second value for object 1: ")
    B = int(input())

    print("Enter first value for object 2: ")
    C = int(input())

    print("Enter second value for object 2: ")
    D = int(input())

    Obj1 = Demo(A,B)
    Obj2 = Demo(C,D)

    Obj1.Fun()
    Obj1.Gun()
    Obj2.Fun()
    Obj2.Gun()

if __name__ == "__main__":
    main()