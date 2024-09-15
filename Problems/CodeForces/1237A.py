n = int(input())
from math import ceil, floor

op = 1
for _ in range(n):
    x = int(input())
    if x%2==0: print(x//2)

    else:
        if op == 1:
            print(ceil(x/2))
            op = 0
        else:
            print(floor(x/2))
            op = 1


