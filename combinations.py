def combinations(n, k):
    
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    
    return result

def fact(x):
   
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if x == 0 or x == 1:
        return 1
    
    result = 1
    for i in range(2, x + 1):
        result *= i
    
    return result