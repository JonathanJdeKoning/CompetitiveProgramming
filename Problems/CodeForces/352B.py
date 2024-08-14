import sys
from collections import defaultdict
from itertools import pairwise
n = int(input())
nums = list(map(int, input().split()))
d = defaultdict(list)

ans = []
for i, c in enumerate(nums):
    d[c].append(i)

for k, v in d.items():
    if len(v) == 1:
        ans.append((k,0))
    elif len(v) == 2:
        ans.append((k,v[1]-v[0]))
    else:
        base = v[1]-v[0]
        for a,b in pairwise(v[1:]):
            if b-a != base:
                break
        else:
            ans.append((k,base))
        continue
print(len(ans))
for a, b in sorted(ans):
    sys.stdout.write(f"{a} {b}\n")
