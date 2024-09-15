R, C = map(int, input().split())

mat = [["#"]*(C+2)]
for _ in range(R):
    mat.append(["#"] + list(input()) + ["#"])

mat.append(["#"]*(C+2))

directions = [(-1,0),(0,-1),(1,0),(0,1)]
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "#": continue
        
        if mat[i+1][j] == "#" and mat[i-1][j] == "#" and mat[i][j+1] == "#" and mat[i][j-1] == "#":
            mat[i][j] = "E"


        if (i+j)%2 == 0 and cell == ".": mat[i][j] = "E"

for row in mat[1:-1]:
    print("".join(row[1:-1]))
