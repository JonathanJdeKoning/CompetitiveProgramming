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

R,C = ints()
M = [list(input()) for _ in range(R)]
look = input()
for row in M:
    if look in "".join(row) or look in "".join(row[::-1]):
        exit(print("YES"))

for i in range(C):
    col = "".join([row[i] for row in M])
    if look in col or look in col[::-1]:
        exit(print("YES"))
print("NO")
