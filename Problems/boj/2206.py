R,C = map(int, input().split())
mat = []
for _ in range(R):
    mat.append(list(map(int, list(input()))))

from collections import deque

q = deque([(0,0,True)])
seen = set()

directions = [(0,1), (1,0),(-1,0),(0,-1)]
end = (R-1, C-1)
steps = 0

while q:
    steps += 1
    for _ in range(len(q)):
        currY,currX, canBreak = q.popleft()
        if (currY, currX, canBreak) in seen: continue
        seen.add((currY, currX, canBreak))
        if (currY, currX) == end:
            exit(print(steps))

        for dy, dx in directions:
            y = currY + dy
            x = currX + dx
            if min(y, x) == -1: continue
            if y==R or x == C: continue

            cell = mat[y][x]
            if (y,x, canBreak) in seen:continue
            
            if cell == 0:
                q.append((y,x,canBreak))
            elif cell == 1 and canBreak:
                q.append((y,x,False))
print(-1)
