
from collections import deque
import sys
input = sys.stdin.readline

C, R, H = map(int, input().split())

box = []
q = deque([])
for k in range(H):
    layer = []
    for i in range(R):
        row = list(map(int, input().split()))
        for j, c in enumerate(row):
            if c == 1:
                q.append((k, i, j))
        layer.append(row)
    box.append(layer)

steps = -1
directions = [(0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
seen = set(q)  # mark all initial ripe tomatoes as seen

while q:
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        # No need to check if curr is in seen because we mark when adding to the queue

        for dh, dy, dx in directions:
            h, y, x = curr[0] + dh, curr[1] + dy, curr[2] + dx

            if 0 <= h < H and 0 <= y < R and 0 <= x < C and box[h][y][x] == 0 and (h, y, x) not in seen:
                q.append((h, y, x))
                seen.add((h, y, x))
                box[h][y][x] = 1

# Check for any unripe tomatoes left
for layer in box:
    for row in layer:
        for cell in row:
            if cell == 0:
                print(-1)
                sys.exit()

print(steps)
