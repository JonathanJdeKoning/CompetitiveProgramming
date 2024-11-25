from math import inf
numCities = int(input())
mat = [[inf]*numCities for _ in range(numCities)]
numBuses = int(input())
for _ in range(numBuses):
    a,b,c = list(map(int, input().split()))
    mat[a-1][b-1] = min(c, mat[a-1][b-1])

for i in range(numCities):
    mat[i][i] = 0
for k in range(numCities):
    for i in range(numCities):
        for j in range(numCities):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

for row in mat:
    row = list(map(lambda x: x if x != inf else 0, row))
    print(" ".join(map(str, row)))