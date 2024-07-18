n =  int(input())
nums = list(map(int, input().split()))

dp = [1]*len(nums)
for i, num in enumerate(nums[1:], start=1):
    for j, check in enumerate(nums[:i]):
        if num < check:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

