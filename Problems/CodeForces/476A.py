n,m = map(int, input().split())
mx = n

from math import ceil, floor
mn = ceil(n/2)

for i in range(mn ,mx+1):
    if i%m==0:
        exit(print(i))
print(-1)
