from collections import Counter, deque, defaultdict, deque
from itertools import pairwise, groupby
from functools import reduce, cache
from math import ceil, floor, sqrt


for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    uniq = set(A)
    if len(uniq) == 1:
        print("NO")
        continue
    mx = max(uniq)
    uniq.discard(mx)
    mx2 = max(uniq)
    fq = Counter(A)
    fq[mx] -= 1
    fq[mx2] -= 1

    new = [mx, mx2]

    for k,v in sorted(fq.items(), reverse = True):
        new.extend([k]*v)
    print("YES")
    print(" ".join(map(str, new )))
    

