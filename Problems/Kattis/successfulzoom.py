N =int(input())
A = list(map(int, input().split()))
from itertools import pairwise
for k in range(1, (N//2)+1):
    new = A[k-1:len(A):k]
    for a,b in pairwise(new):
        if b <= a:
            break
    else: exit(print(k))
print("ABORT!")