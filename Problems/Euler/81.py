from itertools import accumulate
mat = []
with open("mat.txt", "r") as file:
    for line in file.readlines():
        mat.append([int(x) for x in line.split(",")])

dp = [[0]*80 for _ in range(80)]
dp[0] = list(accumulate(mat[0]))

for i in range(1, 80):
    dp[i][0] = dp[i-1][0] + mat[i][0]

for i in range(1, 80):
    for j in range(1, 80):
        dp[i][j] = mat[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])