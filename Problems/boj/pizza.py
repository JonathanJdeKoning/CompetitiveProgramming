h = 0
q = 0
t = 0
ans =0
for _ in range(int(input())):
    s = input()
    if s == "1/2":
        h += 1
    elif s == "1/4":
        q += 1
    else:
        t += 1

d,m = divmod(h, 2)
ans += d
h = m

mn = min(q,t)
ans += mn
q -= mn
t -= mn

ans += t

if h:
    ans += 1
    if q:
        q = max(0,q-2)
from math import ceil
ans += ceil(q/4)
print(ans)
