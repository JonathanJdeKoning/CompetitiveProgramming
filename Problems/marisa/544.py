from functools import cache, reduce
from itertools import pairwise, groupby
from math import ceil, floor, sqrt, gcd, lcm, factorial
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, nlargest, nsmallest

def debug(val, name):   print(f"#{val}# DEBUG{{{name}}}")
def outs(A, delim=" "): print(delim.join(map(str, A)))
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

##########################################################

N = int(input())

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    neg = False
    if n < 0:
        n = -n
        neg = True
    while n:
        digits.append(int(n % b))
        n //= b
    if neg: digits.append("-")
    return digits[::-1]

for i in range(3**N):
    s = "".join(map(str, numberToBase(i, 3))).zfill(N)
    s = s.replace("0","A")
    s = s.replace("1","B")
    s = s.replace("2","C")
    if "AA" not in s and "BB" not in s and "CC" not in s:
        print(s)


