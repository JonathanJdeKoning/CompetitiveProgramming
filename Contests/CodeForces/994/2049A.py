from collections import Counter, deque, defaultdict, deque
from itertools import pairwise, groupby
from functools import reduce, cache
from math import ceil, floor, sqrt


for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    ans = 0
    for k,v in groupby(A, key=lambda x:x>0):
        if k:
            ans += 1
    if ans >2:
        print(2)
    else:
        print(ans)
