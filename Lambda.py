print("Application to demonstrate Anonymous functions or Lambda functions.")

# Normal functions or Named functions
# Syntax :
# def Function_Name(Function_Parameters):
#   Function_Body
def Add(No1,No2):
    return No1+No2

# Lambda functions / Unnamed functions
# Syntax : lambda parameters : Body
AddFunction = lambda A,B : A+B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function : ",Ans1)
print("Addition using lambda function : ",Ans2)

print("Type of Lambda function : ",type(AddFunction))