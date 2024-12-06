from collections import deque, defaultdict, deque
from math import ceil, floor, sqrt
from functools import reduce, cache
from itertools import pairwise, groupby

ans1 = 0
ans2 = 0
mat = [list(line.strip()) for line in open("day6.in", "r")]

R, C = len(mat), len(mat[0])
currdir =(None, None) 
y, x = (None, None)
startY, startX = (None, None)
for i in range(R):
    for j in range(C):
        if mat[i][j] in "><v^":
            if mat[i][j] == ">":
                currdir = (0,1)
            elif mat[i][j] == "<":
                currdir = (0,-1)
            elif mat[i][j] == "^":
                currdir = (-1,0)
            elif mat[i][j] == "v":
                currdir = (1,0)
            mat[i][j] = "."
            y, x = i,j
            startY, startX = i,j

startDir = (currdir[0], currdir[1])
seen = set([(y,x)])
mp = {
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0,-1),
    (0,-1):(-1,0)
}
while True:
    nextY, nextX = currdir[0]+y, currdir[1]+x
    if min(nextY, nextX) == -1 or nextY == R or nextX == C:
        print(len(seen))
        break
    if  mat[nextY][nextX] == "#":
        currdir = mp[currdir]
        continue
    y,x = nextY, nextX
    seen.add((y,x))
seen.discard((startY, startX))
for k, (i,j) in enumerate(seen):
    mat[i][j] = "#"
    seenmp = defaultdict(set)
    y,x  = startY, startX
    currdir = (startDir[0], startDir[1])
    seenmp[(y,x)].add(currdir)
    while True:
        nextY, nextX = currdir[0]+y, currdir[1]+x
        if min(nextY, nextX) == -1 or nextY == R or nextX == C:
            break
        if mat[nextY][nextX] == "#":
            currdir = mp[currdir]
            continue
        y,x = nextY, nextX
        if currdir in seenmp[(y,x)]:
            ans2 += 1
            break
        seenmp[(y,x)].add(currdir)
    mat[i][j] = "."






print(ans1)
print(ans2)