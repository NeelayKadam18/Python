
# Try with traversing the loop in reverse order
class Value:

    def __init__(self,Data):
        self.No = Data

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.No):
            if(self.No%i == 0):
                Sum = Sum + i

        return Sum

    def CheckPerfect(self):
        Ans = self.SumFactors()
        if(self.No == Ans):
            return True
        else:
            return False

    def CheckPrime(self):
        i= 0
        flag = True

        for i in range(2,int(self.No/2)+1):
            if(self.No%i == 0):
                flag = False
                break
         return flag

def main():
    print("Please enter number: ")
    A = int(input())

    obj = Value(A)

    Ret = obj.CheckPrime()
    if(Ret == True):
        print("{} is a prime number".format(A))
    else:
        print("{} is not a prime number".format(A))

if __name__ == "__main__":
    print("Inside starter")
    main()