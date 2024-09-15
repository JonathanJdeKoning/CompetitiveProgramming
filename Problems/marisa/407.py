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

R,C = ints()
M = [[0]*C for _ in range(R)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
y,x = (0,0)
curr = 1
end = R*C
currdir = 0
while True:
    M[y][x] = curr
    curr += 1
    if curr == end+1:break
    
    dy, dx = directions[currdir]
    

    newY, newX = dy+y, dx+x
    if min(newY, newX) == -1 or newY == R or newX == C or M[newY][newX] != 0:
        currdir = (currdir+1)%4
        dy, dx = directions[currdir]
        y+=dy
        x+=dx
    else:
        y = newY
        x = newX

outmat(M)
