R,C = map(int, input().split())
mat = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        cell = mat[i][j]

        if cell == ".":
            if (i+j)%2==0:
                mat[i][j] = "W"
            else:
                mat[i][j] = "B"

for row in mat:
    print("".join(row))
