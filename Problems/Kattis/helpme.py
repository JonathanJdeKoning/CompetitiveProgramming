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

mat = []
for _ in range(16):
    row = input()
    if row == "+---+---+---+---+---+---+---+---+": continue
    mat.append(row.split("|")[1:-1])

white = []
black = []
for i, row in enumerate(mat, start=1):
    for j, cell in enumerate(row):
        let = chr(j+97)
        rr = 9-i

        if cell in ["...", ":::"]: continue
        if cell[1].isupper():
            if cell[1].lower() == "p":
                white.append(f"{let}{rr}")
            else:
                white.append(f"{cell[1]}{let}{rr}")
        else:
            if cell[1].lower() == "p":
                black.append(f"{let}{rr}")
            else:
                black.append(f"{cell[1].upper()}{let}{rr}")
order = "kqrbn"
whitePieces = [x for x in white if len(x) == 3]
whitePawns = [x for x in white if len(x) == 2]
blackPieces = [x for x in black if len(x) == 3]
blackPawns = [x for x in black if len(x) == 2]

whitePieces.sort(key=lambda x: (order.find(x[0].lower()), int(x[2]), x[1]))
blackPieces.sort(key=lambda x: (order.find(x[0].lower()), -int(x[2]), x[1]))

whitePawns.sort(key=lambda x: (int(x[1]), x[0]))
blackPawns.sort(key=lambda x: (-int(x[1]), x[0]))

white = whitePieces + whitePawns
black = blackPieces + blackPawns
print("White: " + ",".join(white))
print("Black: " + ",".join(black))