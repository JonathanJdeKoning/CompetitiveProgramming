from collections import deque, defaultdict, deque, Counter
from math import ceil, floor, sqrt
from functools import reduce, cache
from itertools import pairwise, groupby
for tc in range(int(input())):
    n,m = list(map(int, input().replace(","," ").split()))
    A = list(map(int, input().replace(","," ").split()))
    B = list(map(int, input().replace(","," ").split()))
    
    Bset = set(B)
    ans = 0
    for num in A:
        if num in Bset:
            ans += 1
    print(ans)
