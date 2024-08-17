l, r = map(int, input().split())
from math import gcd
for i in range(l,r+1):
    for j in range(i+1,r+1):
        for k in range(j+1, r+1):
            if gcd(i,j) == 1 and gcd(j,k) == 1 and gcd(i,k) != 1:
                exit(print(i,j,k))
print(-1)


