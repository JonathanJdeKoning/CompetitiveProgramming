from collections import deque
seen = set()
ans = 0
directions=[(-1,0),(1,0),(0,1),(0,1),(1,1),(1,-1),(-1,-1),(-1,1)]
R, C = map(int, input().split())
mat = [list(input()) for _ in range(R)]
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "#" and (i,j) not in seen:
            q = deque([(i,j)])
            while q:
                curr = q.popleft()
                
                currY, currX = curr
                if curr in seen: continue
                seen.add(curr)
                
                for dy, dx in directions:
                    y = dy+currY
                    x = dx+currX

                    if min(y, x) == -1 or y==R or x==C or (y,x) in seen or mat[y][x] != "#": continue
                    
                    q.append((y,x))
print(ans)
