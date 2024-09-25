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

n = int(input())
t = triangle(n)
if t%2==1: xprint("NO")
target = (t//2)
a = set(list(range(1,n+1)))
b = set()
total = 0
curr = 1
if n%2==1:
    while total != target:
        total += curr
        total +=n-curr
        b.add(curr)
        b.add(n-curr)
        a.discard(curr)
        a.discard(n-curr)

        curr += 1
else:
    while total != target:
        total += curr
        total +=(n+1)-curr
        b.add(curr)
        b.add((n+1)-curr)
        a.discard(curr)
        a.discard((n+1)-curr)

        curr += 1
print("YES")
print(len(a))
outs(a)
print(len(b))
outs(b)
