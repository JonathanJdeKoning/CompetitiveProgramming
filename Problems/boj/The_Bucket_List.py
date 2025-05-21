from collections import Counter, deque, defaultdict, deque
from itertools import pairwise, groupby
from functools import reduce, cache
from math import ceil, floor, sqrt

buckets = defaultdict(int)
mx = 0
count = 0
for _ in range(int(input())):
    start, end, buck = list(map(int, input().replace(","," ").split()))
    buckets[start] += buck
    buckets[end] -= buck
    for i in sorted(buckets.keys()):
        count += buckets[i]
        mx = max(mx, count)
print(mx)
