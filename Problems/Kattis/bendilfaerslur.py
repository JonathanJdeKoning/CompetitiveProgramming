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

s = input()
if "." in s: xprint(".".join(s.split(".")[::-1])+".in-addr.arpa.") 

s = s.replace("::", ":dekoding:")
s = s.split(":")
parts = len(s)
for i in range(len(s)):
    part = s[i]
    if part == "dekoding":
        s[i] = "0000"*(9-parts)
    elif len(part) != 4:
        s[i] = part.zfill(4)
#print(s)
out = []
for part in s:
    for c in part:
        out.append(c)
out = out[::-1]
print(".".join(out)+ ".ip6.arpa.") 