import os
import sys
from functools import cache, reduce
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, gcd, lcm, factorial
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from itertools import pairwise, groupby, chain, permutations, combinations

def debug(val, name):   print(f"#{val}# DEBUG{{{name}}}")
def outs(A, delim=" "): print(delim.join(map(str, A)))
def xprint(s):          exit(print(s))
def outmat(M):          list(map(outs, M))
def ints():             return list(map(int, input().split()))
def intmat(R):          return [ints() for _ in range(R)]
def strmat(R):          return [list(input()) for _ in range(R)]
def rotmat(M):          return list(zip(*M[::-1]))
def isPowTwo(n):        return n > 0 and (n & (n - 1)) == 0
def triangle(n):        return (n*(n+1))//2
def allsubs(x):         return [x[i:j] for i in range(len(x)) for j in range(i+1,len(x)+1)]
def factors(n):         return set(reduce(list.__add__,([i,n//i] for i in range(1,int(n**0.5)+1)if n%i==0)))
def nCk(n,k):           return factorial(n)//(factorial(k)*factorial(n-k))
def powerset(s):        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

x,y = ints()
N = int(input())

insts = [input() for _ in range(N)]
l = {(1,0):(0,-1),(-1,0):(0,1), (0,-1):(-1,0),(0,1):(1,0)}
r = {(1,0):(0,1), (-1,0):(0,-1),(0,1):(-1,0),(0,-1):(1,0)}
def simulate(insts):
    y,x = 0,0
    dy,dx = (1,0)

    for i in insts:
        if i == "Forward":
            y += dy
            x += dx
        elif i == "Left":
            dy,dx = l[(dy,dx)]
        else:
            dy,dx = r[(dy,dx)]
    return x,y



for i in range(N):
    old = insts[i]
    for inst in ["Forward", "Left", "Right"]:
        insts[i] = inst
        if simulate(insts) == (x,y):
            exit(print(f"{i+1} {inst}"))
    insts[i] = old


