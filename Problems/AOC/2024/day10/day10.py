mat = [list(map(int, line.strip())) for line in open("day10.in", "r")]
heads = []
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == 0:
            heads.append((i,j,0))

directions = [(-1,0),(0,1),(1,0),(0,-1)]
R, C = len(mat), len(mat[0])
ans1, ans2 = 0, 0
for head in heads:
    dfs = [head]
    ends = set()
    while dfs:
        y,x,curr = dfs.pop()
        if curr == 9:
            ans2 += 1
            ends.add((y,x))
            continue
        for dy, dx in directions:
            nY, nX = dy+y, dx+x 
            if min(nY, nX) == -1 or nY==R or nX==C or mat[nY][nX] != curr+1:
                continue

            dfs.append((nY, nX, curr + 1))
    ans1 += len(ends)
         
print(ans1)
print(ans2)
