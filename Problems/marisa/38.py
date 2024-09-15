from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def inInts(): return list(map(int, input().split()))
def inIntMat(R): return [inInts() for _ in range(R)]
def outInts(A): print(" ".join(map(str, A)))

##########################################################

R, C = inInts()
mat = inIntMat(R)
out = []

for i in range(C):
    out.append(sum([row[i] for row in mat]))
outInts(out)
