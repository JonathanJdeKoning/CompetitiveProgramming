from collections import deque
import sys
C, R, H = map(int, input().split())

box = []
q = deque([])
for k in range(H):
    layer = []
    for i in range(R):
        row = list(map(int, input().split()))
        for j, c in enumerate(row):
            if c == 1:
                q.append((k,i,j))
        layer.append(row)
    box.append(layer)


steps = -1
directions = [(0,0,-1),(0,0,1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
seen = set(q)
while q:
    steps+=1
    for _ in range(len(q)):
        curr = q.popleft()

        for dh, dy, dx in directions:
            h,y,x=curr[0]+dh,curr[1]+dy, curr[2]+dx

            if min(h,y,x) == -1 or h==H or y==R or x==C or box[h][y][x] != 0 or (h,y,x) in seen:
                continue
            q.append((h,y,x))
            box[h][y][x] = 1
            seen.add((h,y,x))

for layer in box:
    for row in layer:
        for cell in row:
            if cell ==0:
                print(-1)
                sys.exit()

print(steps)
