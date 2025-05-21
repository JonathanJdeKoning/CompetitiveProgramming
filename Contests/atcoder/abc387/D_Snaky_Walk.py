from collections import deque
R, C = list(map(int, input().replace(","," ").split()))
mat = []
for i in range(R):
    row = list(input())
    if "S" in row:
        sy, sx = i, row.index("S")
    if "G" in row:
        ey, ex = i, row.index("G")
    mat.append(row)

directions = [(-1,0),(0,1),(1,0),(0,-1)]
seen = set()
steps = 0
q = deque([])
for dy, dx in directions:
    ny, nx = dy+sy, dx+sx
    if min(ny, nx) == -1 or ny == R or nx == C or mat[ny][nx] == "#": continue
    if dy == 0:
        q.append((ny, nx, 1))
    else:
        q.append((ny, nx, 0))


while q:
    steps += 1
    for _ in range(len(q)):
        cy, cx, movedH = q.popleft()

        if (cy, cx, movedH) in seen: continue
        seen.add((cy, cx, movedH))
        if (cy, cx) == (ey, ex):
            exit(print(steps))

        for dy, dx in directions:
            if not movedH and dx == 0: continue
            if movedH and dy == 0: continue

            ny, nx = dy+cy, dx+cx

            if min(ny, nx) == -1 or ny == R or nx == C or mat[ny][nx] == "#": continue
            q.append((ny, nx, abs(movedH-1)))
print(-1)

