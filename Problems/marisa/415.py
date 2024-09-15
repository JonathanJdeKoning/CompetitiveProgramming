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

s = input().split()
ans = 0
for mod in s:
    num = []
    for c in mod:
        if c.isdigit():
            num.append(c)

    try:
        ans += int("".join(num))
    except: pass
print(ans)
