mat = []
for _ in range(6):
    mat.append(list(map(int, input().split())))
mx = -99999
for i in range(4):
    for j in range(4):
        total = 0
        total += sum(mat[i][j:j+3])
        total += sum(mat[i+2][j:j+3])
        total += mat[i+1][j+1]
        mx = max(mx, total)
print(mx)

