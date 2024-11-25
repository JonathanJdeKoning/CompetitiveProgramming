R, C = list(map(int, input().split()))
mat = [list(map(int, input().split())) for _ in range(R)]
new = [[0]*C for _ in range(R)]
for i in range(1,R-1):
    for j in range(1,C-1):
        u,d,l,r = mat[i-1][j], mat[i+1][j], mat[i][j+1], mat[i][j-1]

        if min([u,d,l,r]) > mat[i][j]:
            new[i][j] = 1

for row in new:
    print(" ".join(map(str, row)))