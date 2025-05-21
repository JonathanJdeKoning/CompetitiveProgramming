N, K = list(map(int, input().replace(","," ").split()))
h = list(map(int, input().replace(","," ").split()))
from math import inf
dp = [None]*len(h)

dp[0] = 0
for i in range(1, min(K + 1, len(h))):
    dp[i] = abs(h[0] - h[i])
for i in range(K+1, len(h)):
    best = inf 
    base = h[i]
    for j in range(i-K,i):
        if j >= 0:
            best = min(best, dp[j] + abs(base- h[j]))
        else: break
    dp[i] = best
print(dp[len(h)-1])