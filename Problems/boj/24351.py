from functools import cache

def solve():
    n = int(input())
    s = input()
    valid = set([str(i) for i in range(10,10+n)])
    dp = [0]*(len(s)+1)
    dp[0] = 1
    dp[1] =1
    for i, c in enumerate(s[1:], start=1):
        newnum = s[i-1]+c
        dp[i+1]=dp[i]
        if newnum in valid:
            dp[i+1] += dp[i-1]

    return dp[-1]



print(solve())
