from collections import defaultdict
from math import ceil
N = int(input())
mp = defaultdict(int)
for _ in range(N):
    p, n = input().split()
    mp[p] += int(n)

for k in mp:
    print(k, ceil(mp[k]/64))