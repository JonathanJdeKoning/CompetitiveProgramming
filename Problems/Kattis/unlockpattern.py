mat = []
for i in range(3):
    mat.append(list(map(int, input().split())))

points = {}

for i in range(3):
    for j in range(3):
        points[mat[i][j]] = (i,j)

tot = 0

for i in range(1,9):
    x1 = points[i][0]
    y1 = points[i][1]

    x2 = points[i+1][0]
    y2 = points[i+1][1]

    import math
    tot += math.sqrt((abs(x2-x1)**2 + abs(y2-y1)**2))
print(tot)

