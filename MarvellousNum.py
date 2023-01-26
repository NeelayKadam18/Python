def ChkPrime(Value):
    if Value > 1:
        for i in range(2, int(Value / 2) + 1):
            if ((Value % i) == 0):
                break
        else:
            return Value
