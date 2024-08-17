R,C = map(int, input().split())
strawY = set()
strawX = set()
mat = []
for i in range(R):
    row = list(input())
    for j, cell in enumerate(row):
        if cell == "S":
            strawY.add(i)
            strawX.add(j)
    mat.append(row)

good = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "S": continue
        if j not in strawX or i not in strawY:
            good += 1
print(good)

