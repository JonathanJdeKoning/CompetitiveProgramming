R, C= list(map(int, input().replace(","," ").split()))
mat = [[0]*C for _ in range(R)]

obs = set()
for i in range(R):
    row = list(input())
    for j, cell in enumerate(row):
        if cell =="#": 
            obs.add((i,j))
            mat[i][j] = 0
   
for i in range(R):
    for j in range(C):
        if (i,j) == (0,0):
            mat[i][j] = 1
            continue
        if (i,j) in obs: continue
        left = 0
        up = 0
        if j != 0:
            left = mat[i][j-1]
        if i != 0:
            up = mat[i-1][j]
        mat[i][j] = up + left
print(mat[R-1][C-1]%1000000007) 