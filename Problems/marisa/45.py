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

s = input()
if len(s) <8: exit(print("WEAK"))
l = []
u = []
d = []

for c in s:
    if c.islower():
        l.append(c)
    elif c.isupper():
        u.append(c)
    elif c.isdigit():
        d.append(c)

if all([l,u,d]):
    print("STRONG")
else:
    print("WEAK")
