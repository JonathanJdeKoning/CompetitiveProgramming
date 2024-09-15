from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def inInts(): return list(map(int, input().split()))
def outInts(A): print(" ".join(map(str, A)))
##########################################################

N = int(input())
A = inInts()
fq = Counter(A)
mx = max(fq.values())

for k,v in sorted(fq.items(), reverse=True):
    if v == mx:
        exit(print(k))
