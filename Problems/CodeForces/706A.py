x,y = list(map(int, input().split()))

N = int(input())
from math import inf, sqrt
ans = inf
for _ in range(N):
    tx, ty, tv = list(map(int, input().split()))
    time = (sqrt((ty-y)**2+(tx-x)**2))/tv
    
    ans = min(ans, time)
print(ans)