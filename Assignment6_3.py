
print("Application to demonstrate object oriented programming.\n")

class Numbers:
    def __init__(self,Data):
        self.Value = Data

    def CheckPrime(self):
        i = 0
        flag = True

        for i in range(2, int(self.Value / 2) + 1):
            if (self.Value % i == 0):
                flag = False
                break
        return flag

    def CheckPerfect(self):
        Ans = self.SumFactors()
        if(self.Value == Ans):
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ")
        i = 1
        while (i <= int(self.Value/2)):
            if (self.Value % i == 0):
                print(i,end = " ")
            i = i + 1

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                Sum = Sum + i

        return Sum


def main():
    print("Please enter number: ")
    A = int(input())

    obj = Numbers(A)
    Ret = obj.CheckPrime()

    if(Ret == True):
        print("{} is a prime number.".format(A))
    else:
        print("{} is not a prime number.".format(A))

    Ret = obj.CheckPerfect()

    if (Ret == True):
        print("{} is a perfect number.".format(A))
    else:
        print("{} is not a perfect number.".format(A))

    obj.Factors()

    Sum = obj.SumFactors()
    print("\nSum of all factors is : ",Sum)

if __name__ == "__main__":
    main()