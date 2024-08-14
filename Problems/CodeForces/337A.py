n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

l = 0
r = n-1
from math import inf
ans = inf
while True:
    ans = min(ans, nums[r] - nums[l])
    l += 1
    r += 1
    if r ==len(nums): break
print(ans)
