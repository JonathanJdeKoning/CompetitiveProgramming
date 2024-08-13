n = int(input())
from collections import Counter

nums = list(map(int, input().split()))
count = dict(Counter(nums))
total = 0
for k, v in count.items():
    if v < k:
        total += v
    else:
        total += v-k
print(total)
