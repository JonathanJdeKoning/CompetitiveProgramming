n,m = map(int, input().split())
from math import ceil
until = max(1+ceil(n**0.5), 1+ceil(m**0.5))
count = 0
for a in range(0, until+1):
    for b in range(0, until+1):
        if a*a+b == n and a+b*b == m:
            count += 1
print(count)
