from functools import cache
from itertools import pairwise
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def inInts(): return list(map(int, input().split()))
def outInts(A): print(" ".join(map(str, A)))

N,Q = inInts()
A = inInts()

for _ in range(Q):
    i, n = inInts()

    A.insert(i-1, n)

    outInts(A)
