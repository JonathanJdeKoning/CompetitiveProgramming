from collections import deque
directions = [(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(int(input())):
    C, R, cabbages = map(int, input().split())

    mat = [[0]*C for i in range(R)]
    for _ in range(cabbages):
        cX, cY = map(int, input().split())
        mat[cY][cX] = 1
    seen = set()
    groups = 0
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            if cell == 1 and (i,j) not in seen:
                groups += 1
                q = deque([(i,j)])
                
                while q:
                    for _ in range(len(q)):
                        curr = q.popleft()
                        if curr in seen: continue
                        seen.add(curr)

                        for dy, dx in directions:
                            y, x = curr[0]+dy, curr[1]+dx
                            if min(y,x) == -1 or y==R or x==C or (y,x) in seen or mat[y][x]==0: continue
                            q.append((y,x))

    print(groups)
