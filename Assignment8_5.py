# Factorial using Recursion

def Factorial(No):
    if(No <= 0):
        return 1
    else:
        return (No * Factorial(No-1))

Ret = Factorial(5)
print("Result is : ",Ret)
