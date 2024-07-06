while True:

    C, R = map(int, input().split())
    if C==0 and R==0: break
    mat = []
    for _ in range(R):
        mat.append(list(map(int, input().split())))

    islands = 0

    from collections import deque 
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    seen = set()
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            if cell == 1 and (i,j) not in seen:
                islands += 1

                q = deque([(i,j)])

                while q:
                    curr = q.popleft()
                    if curr in seen: continue
                    seen.add(curr)

                    for dy, dx in directions:
                        y, x = curr[0]+dy, curr[1] + dx

                        if min(y,x) == -1 or y == R or x == C or mat[y][x] == 0 or (y,x) in seen:
                            continue
                        q.append((y,x))
    print(islands)



