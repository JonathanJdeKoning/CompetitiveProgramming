R, C = list(map(int, input().replace(","," ").split()))
pref = [[None]*C for _ in range(R)]
mat =[]
mat.append([0]*(C+1))
for _ in range(R):
    mat.append([0] + list(map(int, input().replace(","," ").split())))
for i in range(1, R+1):
    for j in range(1, C+1):
        mat[i][j] += mat[i-1][j]
        mat[i][j] += mat[i][j-1]
        mat[i][j] -= mat[i-1][j-1]

print("\n".join([" ".join(map(str, row)) for row in mat ]))
