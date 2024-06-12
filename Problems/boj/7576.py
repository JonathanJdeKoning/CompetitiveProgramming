from collections import deque
C, R = map(int, input().split())
directions = [(0,-1),(0,1),(-1,0),(1,0)]
numUnripe = 0
grid = []
q = deque([])
for i in range(R):
    row = list(map(int, input().split()))
    for j, tomato in enumerate(row):
        if tomato == 0: numUnripe += 1
        elif tomato == 1: q.append((i,j))
    grid.append(row)

steps = 0
seen = set()
while q:
    if numUnripe <=0: print(steps); break
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr in seen: continue
        seen.add(curr)
        
        for dy, dx in directions:
            y = curr[0]+dy
            x = curr[1]+dx

            if min(y,x) ==-1 or y==R or x==C or (y,x) in seen: continue
            if grid[y][x] == 0:
                grid[y][x] = 1
                numUnripe -= 1
                q.append((y,x))
else:
    print(-1)


    
