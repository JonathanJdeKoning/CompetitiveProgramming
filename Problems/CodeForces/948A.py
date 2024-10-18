directions = [(0,1),(1,0),(-1,0),(0,-1)]
R,C = list(map(int, input().split()))
mat = []
for _ in range(R):
    row = list(input())
    mat.append(row)

for i in range(R):
    for j in range(C):
        if mat[i][j] == "S":
            for dy, dx in directions:
                y, x = i+dy, j+dx

                if min(y,x) == -1 or y == R or x == C:
                    continue

                if mat[y][x] == "W": exit(print("No"))
print("Yes")
for row in mat:
    print("".join(row).replace(".", "D"))