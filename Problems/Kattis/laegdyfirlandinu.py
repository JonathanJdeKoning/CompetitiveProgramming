rows, cols = map(int, input().split())

mat = []
for _ in range(rows):
    mat.append(list(map(int, input().split())))

low = False
for i, row in enumerate(mat):
    for j, x in enumerate(row):
        if i == 0 or j==0 or i==(rows-1) or j == (cols-1): continue

        if x < mat[i+1][j] and x < mat[i-1][j] and x < mat[i][j+1] and x < mat[i][j-1]:
            low = True

if low:
    print("Jebb")
else:
    print("Neibb")

