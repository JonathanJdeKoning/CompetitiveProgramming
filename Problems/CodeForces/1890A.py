import os
import sys
from typing import Any, Callable
from functools import cache, reduce
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, gcd, lcm, factorial
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from itertools import pairwise, groupby, chain, permutations, combinations

OUTPUT, RESET = '[92m', '[0m'
LOCAL = os.path.isfile('C:\\Users\\jj720\\cp.flag')
ogprint = print
print: Callable[[Any],None] = lambda text='', *args, **kwargs: ogprint(f"{OUTPUT}{text}{RESET}", *args, **kwargs) if LOCAL else ogprint(text, *args, **kwargs)
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

##########################################################

def solve():
    N = int(input())
    A = ints()
    fq = Counter(A)

    if len(fq) > 2: return "No"
    if len(fq) == 1: return "Yes"

    if abs(list(fq.values())[0] - list(fq.values())[1]) > 1:
        return "No"
    else:
        return "Yes"
    



for _ in range(int(input())):
    print(solve())