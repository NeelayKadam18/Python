#def Display(No):
#    while(No > 0):
#        print(No)
#        No = No - 1

# Tail Recursion Example
def Display(No):
    if(No > 0):
        print(No)
        No = No - 1
        Display(No)

Display(5)

