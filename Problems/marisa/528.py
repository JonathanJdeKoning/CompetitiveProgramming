from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def inInts(): return list(map(int, input().split()))
def outInts(A): print(" ".join(map(str, A)))
##########################################################

N, Q = inInts()
A = inInts()
qs = []
for _ in range(Q):
    i,j = inInts()
    i -= 1
    j -= 1
    qs.append((i,j))

while qs:
    i,j = qs.pop()
    A[i], A[j] = A[j], A[i]

outInts(A)
