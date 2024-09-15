from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def inInts(): return list(map(int, input().split()))
def outInts(A): print(" ".join(map(str, A)))
##########################################################

N = int(input())
base = [1]

for _ in range(N):
    outInts(base)
    base = [0]+base+[0]
    new = []
    for a,b in pairwise(base):
        new.append(a+b)
    base = new

