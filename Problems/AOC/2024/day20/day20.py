base = 9416
from collections import deque

mat = [list(line.strip()) for line in open("day20.in", "r")]
R, C = len(mat), len(mat[0])
directions = [(-1,0),(0,1),(1,0),(0,-1)]

sy, sx = None, None
ey, ex = None, None
for i, row in enumerate(mat):
    if "S" in row: sy, sx = i, row.index("S")
    if "E" in row: ey, ex = i, row.index("E")

q = deque([(sy, sx, 0, (-1,-1,-1,-1))])
seen = set()
cheats = 0
used = set()
z = 0
while q:
    z += 1
    if z%50000==0:
        print(len(q))
    currY, currX, pico, cheat = q.popleft()
    if pico > base: continue
    if (currY, currX, cheat) in seen: continue
    seen.add((currY, currX, cheat))
    if (currY, currX) == (ey, ex):
        if pico <= base - 100:
            cheats += 1
            print(f"cheat {cheats}")
            continue

    for dy, dx in directions:
        y,x = dy+currY, dx+currX
        if min(y, x) == -1 or y == R or x == C or (y, x, cheat) in seen:
            continue
        if mat[y][x] == "#":
            if cheat != (-1,-1,-1,-1): continue
            if (y,x,dy,dx) in used: continue
            else: 
                q.append((y,x, pico+1, (y,x,dy,dx)))
                used.add((y,x, dy,dx))
                continue
        else:
            q.append((y,x, pico+1, cheat))
print(cheats)
