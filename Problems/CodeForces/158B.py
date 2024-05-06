from collections import Counter, defaultdict
from math import ceil
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
c = {1:0,2:0,3:0,4:0}
count = dict(Counter(nums))
for k, v in count.items():
    c[k] = v
total = c[4]
total += c[3]
c[1] -= c[3]
if c[1] < 0: c[1] = 0
total += ceil(c[2]/2)
total += ceil(c[1]/4)
print(total)
