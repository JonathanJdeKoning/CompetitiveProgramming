N = int(input())
nums = list(map(int, input().replace(","," ").split()))

if len(nums) == 1:exit(print(nums[0]))
dp = [0]*len(nums)
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])

for i in range(2, len(nums)):
    dp[i] = max(dp[i-1], nums[i]+dp[i-2])
print(sum(nums) - max(dp))
