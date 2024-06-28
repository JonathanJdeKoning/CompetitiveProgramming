n = int(input())
# 10 9 2 5 3 7 101 18
nums = list(map(int, input().split()))
dp = [1]*(len(nums))
for i, num in enumerate(nums[1:], start=1):
    for j, res in enumerate(dp[:i]):
        if num > nums[j]:
            dp[i] = max(dp[i], res+1)

print(max(dp))
