from functools import lru_cache

def fibonacci_dp(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[-1]+f[-2])
    return f[-1]
    
@lru_cache(maxsize=128)
def fibonnacci_recursion(n):
    if n < 0:
        print("incorrect")
    elif n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonnacci_recursion(n-1) + fibonnacci_recursion(n-2)


import math
def fibonnacci_math(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi,n)/math.sqrt(5))

print(fibonacci_dp(9))
print(fibonnacci_recursion(9))
print(fibonnacci_math(9))