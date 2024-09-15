from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name):   print(f"#{val}# DEBUG{{{name}}}")
def ints():             return list(map(int, input().split()))
def intmat(R):          return [ints() for _ in range(R)]
def outs(A, delim=" "): print(delim.join(map(str, A)))
def outmat(M):          list(map(outs, M))
def rotmat(M):          return list(zip(*M[::-1]))
def allsubs(x):         return[x[i:j] for i in range(len(x)) for j in range(i+1,len(x)+1)]

##########################################################
enc = input()
dec = input()

out = []
for k,v in groupby(enc):
    out.append(len(list(v)))
    out.append(k)
outs(out, "")

inter = []
for k,g in groupby(dec, key=lambda x: x.isdigit()):
    inter.append("".join(list(g)))
out = []
for i in range(0, len(inter), 2):
    out.append(int(inter[i])*inter[i+1])

outs(out, "")
