n,k  = map(int, input().split())
from math import inf
mx = -inf
for _ in range(n):
    f,t = map(int, input().split())

    if t > k:
        mx = max(mx,f- (t-k))
    else:
        mx = max(mx, f)
print(mx)
