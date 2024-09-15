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

points = set()
for _ in range(int(input())):
    x1,y1,x2,y2 = ints()
    
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            points.add((j, i))

print(len(points))

