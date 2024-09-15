R, C = map(int, input().split())

mat = [list(input()) for _ in range(R)]
from math import inf
u,l,r,d = inf,inf,-inf,-inf

for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "*":
            u = min(i, u)
            d = max(i,d)
            l = min(l, j)
            r = max(r, j)

new = []

for i in range(u, d+1):
    new.append(mat[i][l:r+1])

for row in new:
    print("".join(row))


