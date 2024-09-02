n = int(input())
from math import inf

mn =  inf
mx = -inf
ans = -1
for i in range(1,n+1):
    l, r = map(int, input().split())

    if l <= mn and r >= mx:
        ans = i
    elif l < mn:
        mn = l
        ans = -1
    elif r > mx:
        mx = r
        ans = -1

    mn = min(mn, l)
    mx = max(mx, r)

print(ans)
