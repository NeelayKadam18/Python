def Display(No):
    Cnt = 0
    if(Cnt < No):                         # Change while to if
        print("Hello")
        Cnt = Cnt + 1
        Display(No)                       # Call same function in the end

Display(4)