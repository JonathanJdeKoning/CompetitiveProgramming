cardCount, n = map(int, input().split())
from math import inf
best = inf
nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            tot = nums[i]+nums[j]+nums[k]
            if tot > n: continue
            best = min(best, n-tot)
print(n-best)
