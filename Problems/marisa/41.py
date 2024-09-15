from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def ints(): return list(map(int, input().split()))
def intmat(R): return [ints() for _ in range(R)]
def outs(A, delim=" "): print(delim.join(map(str, A)))
def outmat(M): list(map(outs, M))

##########################################################

N,M,Q = ints()

M = intmat(N)

for _ in range(Q):
    q,i,j = ints()
    i-=1
    j-=1
    if q == 1:
        M[i], M[j] = M[j], M[i]
    else:
        for row in M:
            row[i], row[j] = row[j], row[i]
outmat(M)
