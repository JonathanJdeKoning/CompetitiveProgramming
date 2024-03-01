mat = []
for i in range(4):
    mat.append(list(input()))
found = False 
for i in range(3):
    for j in range(3):
        pos = mat[i][j]
        total = 0
        if mat[i][j+1] == pos:
            total += 1
        if mat[i+1][j] == pos:
            total += 1
        if mat[i+1][j+1] == pos:
            total += 1
        if total >=2 or total == 0:
            found = True
if found:
    print("YES")
else:
    print("NO")
