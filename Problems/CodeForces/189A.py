n,a,b,c = map(int, input().split())
from math import inf

a,b,c = sorted([a,b,c])

dp = [-inf]*(n+1)
dp[0] = 0
for i in range(1,n+1):
    if i < a: dp[i] = -inf
    
    minA = -inf if i-a < 0 else dp[i-a]
    minB = -inf if i-b < 0 else dp[i-b]
    minC = -inf if i-c < 0 else dp[i-c]

    dp[i] = 1+max(minA, minB, minC)

print(dp[n])



   
