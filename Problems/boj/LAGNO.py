# Created by Jonathan de Koning on 2025-01-02 [>_]

mat = [list(input()) for _ in range( 8 )]
directions = [(x,y) for x in (-1,0,1) for y in (-1,0,1) if (x,y) != (0,0)]
mxScore = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell != ".": continue
        cellScore = 0
        for dy, dx in directions:
            for mul in range(1, 9):
                ny, nx = i+dy*mul, j+dx*mul
                if min(ny, nx) == -1 or max(ny, nx) >= 8 or mat[ny][nx] == ".":
                    break
                if mat[ny][nx] == "B":
                    cellScore += mul-1
                    break
        mxScore = max(mxScore, cellScore)
print(mxScore)
                


