n, c = map(int, input().split())
nums = list(map(int, input().split()))
from collections import Counter
count = Counter(nums)
idx = {}
for i, num in enumerate(nums):
    if num not in idx:
        idx[num] = i
nums = sorted(nums, key=lambda x:(-count[x], idx[x]))
print(" ".join(map(str, nums)))
