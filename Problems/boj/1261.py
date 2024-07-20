from collections import deque

q = deque([((0,0),0)])
totalWalls = 0

mat = []
C,R = map(int, input().split())
directions = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(R):
    mat.append(list(map(int, list(input()))))
seen = set()
while q:
    for _ in range(len(q)):
        (currY, currX), walls = q.popleft()
        if (currY, currX)==(R-1, C-1): print(walls); exit(0)
        if (currY, currX) in seen: continue
        seen.add((currY, currX))

        for dy, dx in directions:
            y = currY+dy
            x = currX+dx

            if min(y, x)==-1 or y==R or x==C or (y,x) in seen:continue
            if mat[y][x]==1:
                q.append(((y,x),walls+1))
            else:
                q.appendleft(((y,x),walls))

