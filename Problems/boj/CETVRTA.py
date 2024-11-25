xs =[]
ys = []
for _ in range(3):
    x,y = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)

ans = []
from collections import Counter
xfq = Counter(xs)
for k,v in xfq.items(): 
    if v ==1:
        ans.append(k)

yfq = Counter(ys)
for k,v in yfq.items():
    if v == 1:
        ans.append(k)

print(*ans)