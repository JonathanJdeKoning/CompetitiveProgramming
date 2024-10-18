regions = [list(input()) for _ in range(10)]
mat = [list(input()) for _ in range(10)]
for row in mat:
    if row.count("*") != 2:
        exit(print("invalid"))
for i in range(10):
    col = [row[i] for row in mat]
    if col.count("*") != 2: exit(print("invalid"))

reg = {str(i):0 for i in range(10)}
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(10):
    for j in range(10):
        if mat[i][j] != "*": continue
        reg[regions[i][j]] += 1

        for dy, dx in directions:
            y, x = i+dy, j+dx

            if min(y,x) == -1 or y == 10 or x == 10: continue
            if mat[y][x] == "*": exit(print("invalid"))

for k,v in reg.items():
    if v != 2:
        exit(print("invalid"))

print("valid") 