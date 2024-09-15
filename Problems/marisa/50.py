from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def ints(): return list(map(int, input().split()))
def intmat(R): return [ints() for _ in range(R)]
def outs(A, delim=" "): print(delim.join(map(str, A)))
def outmat(M): list(map(outs, M))
def rotmat(M): return list(zip(*M[::-1]))

##########################################################

fq = Counter(input().lower())
out = []
for c in "abcdefghijklmnopqrstuvwxyz":
    out.append(fq[c])

outs(out)
