base = 9416
#base = 84
cheatlength = 20
timesave = 100
from collections import deque

mat = [list(line.strip()) for line in open("day20.in", "r")]
R, C = len(mat), len(mat[0])
best = [[-1]*C for _ in range(R)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]

sy, sx = None, None
ey, ex = None, None
for i, row in enumerate(mat):
    if "S" in row: sy, sx = i, row.index("S")
    if "E" in row: ey, ex = i, row.index("E")



seen = set()
q = deque([(ey,  ex , 0)])
spots = []
while q:
    currY, currX, mn = q.popleft()
    if (currY, currX) in seen: continue
    seen.add((currY, currX))
    best[currY][currX] = mn
    spots.append((currY, currX, mn))
    for dy, dx in directions:
        y, x = dy+currY, dx+currX
        if min(y, x) == -1 or y == R or x == C or mat[y][x] == "#" or (y,x) in seen: continue
        q.append((y,x, mn+1))



ans = 0
seen = set()
q = deque([(sy, sx, 0)])
while q:
    currY, currX, pico = q.popleft()

    if (currY, currX) in seen: continue
    if pico > base - timesave:
        continue
    seen.add((currY, currX))


    for dy, dx in directions:
        y,x = dy+currY, dx+currX
        if min(y,x) == -1 or y == R or x == C or (y, x) in seen or mat[y][x] == "#": continue

        q.append((y, x, pico+1))
    
    ans += len([spot for spot in spots if (dist:=abs(spot[0]- currY) + abs(spot[1] - currX)) <= cheatlength and (dist+pico+spot[2] <= base-timesave)])


print(ans) #285






