from math import gcd, inf
from collections import Counter
def phi(n):
    count = 0

    for i in range(1,n+1):
        if gcd(i,n) == 1:
            count += 1
    return count

ans = [0]*10000001
for i in range(1,3163):
    p = phi(i)
    ans[i] = p

mnrat = inf
for i in range(3163):
    for j in range(3163):
        if i*j <=3163: continue
        if gcd(i,j) ==1:
            phi = ans[i]*ans[j]
            n = i*j
            if Counter(str(n)) == Counter(str(phi)):
                if n/phi < mnrat:
                    mnrat = n/phi
                    print(n)

