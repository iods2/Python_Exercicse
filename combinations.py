import math

def combinations(n, k):

    return math.comb(n, k)

def fact(x):
    
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if x == 0 or x == 1:
        return 1
    
    return x * fact(x - 1)