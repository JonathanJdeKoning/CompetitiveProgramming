memo = []
for i in range(21):
    memo.append([0]*21)
memo[0][0] = 1
for i in range(21):
    for j in range(21):
        up = memo[i-1][j] if i > 0 else 0
        left = memo[i][j-1] if j > 0 else 0
        memo[i][j] += up+left
print(memo[-1][-1])