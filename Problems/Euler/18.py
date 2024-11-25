tri = []
dp = []
with open("triangle.txt", "r") as file:
    for line in file.readlines():
        row = list(map(int, line.split()))
        tri.append(row)
        dp.append([0]*len(row))


dp[0][0] = tri[0][0]

for i, row in enumerate(tri[1:], start=1):
    for j, cell in enumerate(row):
        left = j-1
        l = 0
        r = 0
        if left != -1: l = dp[i-1][left]
        if j != len(row)-1: r = dp[i-1][j]

        dp[i][j] = cell + max(l,r)

print(dp)

print(max(dp[-1]))