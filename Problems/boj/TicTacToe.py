mat = [list(input()) for _ in range(3)]
diag1 = []
diag2 = []
for i in range(3):
    row = mat[i]
    col = [row[i] for row in mat]
    diag1.append(mat[i][i])
    diag2.append(mat[2-i][i])
    if (len(set(row)) == 1 and "." not in row )or (len(set(col)) == 1 and "." not in col): exit(print("YES"))

if (len(set(diag1)) == 1 and "." not in diag1) or (len(set(diag2)) == 1 and "." not in diag2): exit(print("YES"))
print("NO")

    