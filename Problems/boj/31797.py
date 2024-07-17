n, m  = map(int, input().split())

from collections import deque

nums = [0]*(m*2)

for i in range(1,m+1):
    a,b = map(int, input().split())
    nums[a-1] = i
    nums[b-1] = i

nums = deque(nums)
nums.rotate(-(n+1))
print(nums[n-1])
