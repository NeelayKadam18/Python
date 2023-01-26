import sys
print(sys.getrecursionlimit())     #Number of stack frames(Maximum number of function call)

sys.setrecursionlimit(4000)
print(sys.getrecursionlimit()) 