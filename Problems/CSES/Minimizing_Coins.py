from math import inf
N, K = map(int, input().split())
coins = list(map(int, input().split()))
dp = [inf]*(K+1)
dp[0] = 0
for i in range(1, len(dp)):
    dp[i] = 1 + min([dp[i-coinVal] for coinVal in coins if i-coinVal >= 0], default=inf)

ans = dp[-1]
if ans == inf: print(-1)
else:print(ans)
