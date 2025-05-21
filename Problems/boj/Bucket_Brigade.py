from collections import deque


for i in range(10):
    row = input()
    for j in range(10):
        cell = row[j]
        if cell == "B":
            by,bx = i,j
        if cell == "L":
            ly, lx  = i, j
        if cell == "R":
            ry, rx = i, j

q = deque([(by,bx)])
steps = -1
directions = [(-1,0),(0,1),(1,0),(0,-1)]
seen = set()
while q:
    steps += 1
    for _ in range(len(q)):
        cy, cx = q.popleft()
        if (cy,cx) in seen: continue
        seen.add((cy,cx))
        if (cy,cx) == (ly, lx): exit(print(steps - 1 ))
        for dy, dx in directions:
            ny, nx = dy+cy, dx+cx
            if min(ny, nx) == -1 or max(ny, nx) == 10 or (ny, nx) in seen or (ny,nx) == (ry, rx): continue
            q.append((ny, nx))
