n = int(input())
holds = list(map(int, input().split()))
from math import inf
from itertools import pairwise
best = inf


for i in range(1, n-1):
    mx = 0
    for a,b in pairwise(holds[:i]+ holds[i+1:]):
        mx = max(mx, b-a)
    best = min(best, mx)
print(best)
