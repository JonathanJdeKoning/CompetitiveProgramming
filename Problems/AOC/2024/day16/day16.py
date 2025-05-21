import heapq
from collections import defaultdict 
from math import inf
sy, sx = None, None
ey, ex = None, None
mat = [list(line.strip()) for line in open("day16test2.in", "r")]
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "S":
            sy, sx = i, j
        if cell == "E":
            ey, ex = i,j

from collections import deque
parents = defaultdict(list)
h = [(0, sy, sx, 0, 1, -1, -1)]
seen = defaultdict(int)
while h:
    cc, cy, cx, dy, dx, py, px = heapq.heappop(h)
    if (cy, cx) == (7,14) or (cy, cx) == (7,15) or (cy, cx) == (8, 15):
        pass
    if mat[cy][cx] == "#": continue
    if (cy,cx, dy, dx) in seen:
        if cc > seen[(cy, cx, dy, dx)]:
            continue
        else:
            if (py,px, dy, dx) in parents[(cy,cx, dy, dx)]: continue
            parents[(cy,cx, dy, dx)].append((py,px, dy, dx))
            continue

    parents[(cy,cx, dy, dx)].append((py,px, dy, dx))
    seen[(cy, cx, dy, dx)] = cc
    next_step = (cc+1, cy+dy, cx+dx, dy,dx,cy,cx)
    heapq.heappush(h, next_step)
    if dy == 0:
        heapq.heappush(h,(cc+1001, cy+1, cx, 1,  0, cy, cx))
        heapq.heappush(h,(cc+1001, cy-1, cx,-1,  0, cy, cx))
    else:
        heapq.heappush(h,(cc+1001, cy, cx+1, 0,  1, cy, cx))
        heapq.heappush(h,(cc+1001, cy, cx-1, 0, -1, cy, cx))


enddirs = [seen[(ey,ex, 0,1)], seen[(ey,ex, 0,-1)], seen[(ey,ex, 1,0)], seen[(ey,ex, -1,0)]]
print(enddirs)
q = deque([(enddirs[0],ey, ex, 0,1), (enddirs[1], ey, ex, 0,-1), (enddirs[2], ey, ex, 1,0), (enddirs[3], ey, ex, -1,0)])

while q:
    curr, cy, cx, dy, dx = q.popleft()
    if curr != seen[(cy, cx, dy, dx)]:
        continue
    if mat[cy][cx] == "#": continue
    mat[cy][cx] = "█"
    q.append((curr - 1, cy-dy, cx-dx, dy, dx))

    if dy == 0:
        q.append((curr -1001, cy+1, cx, dy-1, dx))
        q.append((curr -1001, cy-1, cx, dy+1, dx))
    else:
        q.append((curr -1001, cy, cx+1, dy, dx-1))
        q.append((curr -1001, cy, cx-1, dy, dx+1))

for row in mat:
    print("".join(row))

