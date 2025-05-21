R, C = list(map(int, input().replace(","," ").split()))
mat = [list(map(int, input().split())) for _ in range(R)]

rows = [sum(row) for row in mat]
cols = []

for i in range(C):
    col = [row[i] for row in mat]
    cols.append(sum(col))


new = [[None]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        cell = rows[i] + cols[j] - mat[i][j]
        new[i][j] = cell


print("\n".join([" ".join(map(str, row)) for row in new ]))


