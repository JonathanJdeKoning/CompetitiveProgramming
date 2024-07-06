from functools import cache

@cache
def numways(n):
    if n < 2 or n%2==1: return 0 
    if n == 2:
        return 3
    return 3*numways(n-2)

print(numways(int(input())))
    
