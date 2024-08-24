n = int(input())

mat = [list(input()) for _ in range(n)]
diag = []
non = []
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if i==j or j==(n-i)-1:
            diag.append(cell)
        else:
            non.append(cell)
from collections import Counter


cD = Counter(diag)
cN = Counter(non)
if len(cD) == 1 and len(cN) == 1:
    if list(cD.keys())[0] != list(cN.keys())[0]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
