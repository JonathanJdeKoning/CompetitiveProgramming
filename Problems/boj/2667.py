n = int(input())
mat = []
clusts = []
for _ in range(n):
    mat.append(list(map(int, input())))

directions = [(-1,0),(1,0),(0,1),(0,-1)]
seen = set()
from collections import deque
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == 0 or (i,j) in seen: continue
        total = 0
        q = deque([(i,j)])
        while q:
            currY, currX = q.popleft()
            if (currY, currX) in seen: continue
            seen.add((currY, currX))
            total += 1

            for dy, dx in directions:
                y = dy+currY
                x = dx+currX

                if min(y,x) ==-1 or y==n or x==n or mat[y][x]==0 or (y,x) in seen: continue
                q.append((y,x))
        clusts.append(total)
print(len(clusts))
print("\n".join(map(str, sorted(clusts))))














