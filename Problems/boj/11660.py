n, q = map(int, input().split())
mat = [[0]*(n+1)]
from itertools import accumulate
for _ in range(n):
    mat.append([0]+list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1,n+1):
        mat[i][j] += mat[i-1][j]
        mat[i][j] += mat[i][j-1]
        mat[i][j] -= mat[i-1][j-1]
for _ in range(q):
    y1,x1,y2,x2 = map(int, input().split())
    main = mat[y2][x2]
    topSub = mat[y1-1][x2]
    leftSub = mat[y2][x1-1]
    redo = mat[y1-1][x1-1]
    res = mat[y2][x2] - topSub - leftSub + mat[y1-1][x1-1]
    print(res)
