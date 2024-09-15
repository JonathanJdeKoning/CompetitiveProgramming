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

d = []
for a,b in pairwise(A):
    d.append(int(b>a))

g = list(groupby(d))
if not g or (len(g) == 2 and g[0][0] == 1 and g[1][0] == 0) or (len(g)==1 and g[0][0] == 1):
    print("YES")
else:
    print("NO")
