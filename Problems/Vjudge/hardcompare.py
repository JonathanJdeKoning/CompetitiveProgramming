a,b,c,d = map(int, input().split())
from math import log
print(b*log(a))
print(d*log(c))
if b*log(a) > d*log(c):
    print("YES")
else:
    print("NO")
