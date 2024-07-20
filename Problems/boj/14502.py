R, C = map(int, input().split())
base = []
avail = []
viruses = []
for i in range(R):
    row = list(map(int, input().split()))
    for j, cell in enumerate(row):
        if cell == 0:
            avail.append((i,j))
        elif cell == 2:
            viruses.append((i,j))
    base.append(row)


def nSafe(mat):
    total = 0
    for row in mat:
        total+= row.count(0)
    return total

from collections import deque
from copy import deepcopy

mx = 0
directions = [(0,-1),(0,1),(1,0),(-1,0)]

from itertools import combinations
walls = combinations(avail, 3)

for triplet in walls:
    mat = deepcopy(base)
    for wallY, wallX in triplet:
        mat[wallY][wallX] = 1
    
    seen = set()

    q = deque(viruses)
    while q:
        for _ in range(len(q)):
            currY, currX = q.popleft()
            if (currY, currX) in seen: continue
            seen.add((currY, currX))
            mat[currY][currX] = 2
            
            for dy, dx in directions:
                y=dy+currY
                x = dx+currX

                if min(y,x)==-1 or y==R or x==C or (y,x) in seen or mat[y][x] != 0: continue
                q.append((y,x))
    mx = max(mx, nSafe(mat))
    
print(mx)


                    




