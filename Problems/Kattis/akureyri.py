N = int(input())
from collections import Counter, deque, defaultdict, deque
from itertools import pairwise, groupby
from functools import reduce, cache
from math import ceil, floor, sqrt

m = defaultdict(int)
for _ in range(N):
    input()
    m[input()] += 1

for k, v in m.items():
    print(k, v)
