n = 200
coins = [200,100,50,20,10,5,2,1]
dp = [0] * (n + 1)
dp[0] = 1

for coin in coins:
    for j in range(coin, n + 1):
        dp[j] += dp[j - coin]

print(dp[n])

