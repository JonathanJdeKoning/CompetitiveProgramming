dp = [0,1,2,4,8,16,32]
N = int(input())
if N < 7: exit(print(dp[N]))
prev = sum(dp)
for i in range(7, N+1):
    dp.append(prev)
    prev *= 2
    prev -= dp[i-6]
    prev = prev % int(1e9+7)

print(dp[-1])