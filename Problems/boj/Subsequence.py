from functools import cache
from itertools import accumulate
from math import inf
N, K = list(map(int, input().replace(","," ").split()))
A = list(map(int, input().replace(","," ").split()))
if sum(A) < K: exit(print(0))

ans = inf
l = 0
r = 0
tot = A[0]
while True:
    if tot < K:
        r += 1
        if r == len(A): break
        tot += A[r]
    else:
        ans = min(ans, (r-l)+1)
        tot -= A[l]
        l += 1
        if l == len(A): break
print(ans)
