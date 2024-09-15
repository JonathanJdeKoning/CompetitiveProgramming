n = int(input())
nums = [int(input()) for _ in range(n)]
if len(nums) < 3:
    print(sum(nums)); exit(0)
dp = [0]*len(nums)
dp[0] = nums[0]
dp[1] = nums[1]+nums[0]
for i, glass in enumerate(nums[2:],start=2):
    dp[i] = max():wq



