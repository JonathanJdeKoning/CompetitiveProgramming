k = int(input())
from collections import defaultdict

d = defaultdict(int)
d["."] =0

for _ in range(4):
    for c in input():
        if c != ".":
            d[c] += 1


mx = max(d.values())
if mx > k*2:
    print("NO")
else:
    print("YES")
