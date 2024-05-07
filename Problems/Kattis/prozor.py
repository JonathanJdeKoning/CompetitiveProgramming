rows, cols, size = map(int, input().split())
mat = []
for _ in range(rows):
    mat.append(list(input()))
mx = 0
mxi=None
mxj=None
for i, row in enumerate(mat[:-(size-1)]):
    for j, cell in enumerate(row[:-(size-1)]):
        total = 0
        for newrow in mat[i+1:(i+size)-1]:
            total += newrow[j+1:j+size-1].count("*")
        if total > mx:
            mx = total
            mxi = i
            mxj = j
print(mx)

mat[mxi][mxj+size-1] = "+"
mat[mxi+size-1][mxj] = "+"
mat[mxi][mxj] = "+"
mat[mxi+size-1][mxj+size-1] = "+"

for j in range(mxj+1,mxj+size-1):
    mat[mxi][j] = "-"
    mat[mxi+size-1][j] = "-"

for i in range(mxi+1, mxi+size-1):
    mat[i][mxj] = "|"
    mat[i][mxj+size-1] = "|"

for row in mat:
    print("".join(row))
