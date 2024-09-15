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

s = list(input())
k = int(input())

def rot(c):
    if c == " ": return " "
    n = ord(c) - ord("a")
    n = (n+k)%26
    return chr(n + ord("a"))

print("".join([rot(x) for x in s]))
