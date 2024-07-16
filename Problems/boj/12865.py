def knapSack(W, wt, val, n):
    dp = [0]*(W+1)
    for i in range(1, n+1):
        for w in range(W, 0, -1):
            if wt[i-1] <= w:
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
    return dp[W]


n, W = map(int, input().split())
profit = []
weight = []
for _ in range(n):
    p,w = map(int, input().split())
    weight.append(p)
    profit.append(w)
print(knapSack(W, weight, profit, n))


