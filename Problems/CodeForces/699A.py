n = int(input())
s = input()
a = list(map(int, input().split()))
from itertools import pairwise
from math import inf
mn = inf
for x, y in pairwise(list(range(n))):
    if s[x] == "R" and s[y]=="L":
        mn = min(mn, (a[y]-a[x])//2)

if mn == inf:
    print(-1)
else:
    print(mn)



