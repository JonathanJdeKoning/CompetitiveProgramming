from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def ints(): return list(map(int, input().split()))
def intmat(R): return [ints() for _ in range(R)]
def outs(A, delim=" "): print(delim.join(map(str, A)))
def outmat(M): list(map(outs, M))

##########################################################

directions = [(1,1),(-1,-1),(1,-1),(-1,1)]
N,M,X,Y = ints()
X -= 1
Y -= 1
A = intmat(N)
oldX, oldY = X,Y
tot = A[X][Y]
for dy, dx in directions:
    X,Y = oldX, oldY

    while True:
        newY, newX = Y+dy, X+dx
        if min(newY, newX) == -1 or newY == M or newX == N:
            break
        tot += A[newX][newY]
        Y, X = newY, newX
print(tot)
