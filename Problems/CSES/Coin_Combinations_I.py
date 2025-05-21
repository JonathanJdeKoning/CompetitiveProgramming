numCoins, target = map(int, input().split())
coins = sorted(list(map(int, input().split())))
dp = [0]*(target+1)
dp[0] = 1
for i in range(1, target+1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] += dp[i - coin]
        else: break
print(dp[target]%int(1e9+7))