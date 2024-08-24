n = int(input())

mat = [[0]*(n+1)]
for _ in range(n):
    mat.append([0]+ list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1, n+1):
        mat[i][j] += max(mat[i-1][j], mat[i][j-1])

for row in mat:
    print(row)

