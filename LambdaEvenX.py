print("Application to demonstrate Anonymous functions or Lambda functions.")

Even = lambda No : No%2 == 0
Ret = Even(12)

if(Ret == True):
    print("Its even")
else:
    print("Its odd")