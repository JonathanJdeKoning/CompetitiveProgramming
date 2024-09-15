n = int(input())

mat = [["."]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            mat[i][j] = "C"
from math import ceil
print(ceil(n*(n/2)))
for row in mat:
    print("".join(row))
