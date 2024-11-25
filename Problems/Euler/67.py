from functools import lru_cache
@lru_cache(maxsize=None)
def f(n): # based on second formula in A018805
    if n == 0:
        return -1
    c, j = 2, 2
    k1 = n//j
    while k1 > 1:
        j2 = n//k1 + 1
        c += (j2-j)*(2*f(k1)+1)
        j, k1 = j2, n//j2
    return (n*(n-1)-c+j)//2 

print(f(1000000))