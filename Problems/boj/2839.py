from functools import cache
n = int(input())
from math import inf
@cache
def solve(n):
    if n < 3: return inf
    if n == 3 or n == 5: return 1
    
    return 1 + min(solve(n-3),solve(n-5))
res = solve(n)
if res is inf:
    print(-1)
else:
    print(res)
