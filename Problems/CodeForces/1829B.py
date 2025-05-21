from collections import Counter, deque, defaultdict, deque
from itertools import pairwise, groupby
from functools import reduce, cache
from math import ceil, floor, sqrt


for tc in range(int(input())):
    mx = 0
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    for k, v in groupby(A):
        if k == 0:
            mx = max(mx, len(list(v)))
    print(mx)
    