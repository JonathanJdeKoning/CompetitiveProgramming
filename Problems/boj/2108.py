import sys
input = sys.stdin.readline
from collections import defaultdict
count = defaultdict(int)
most = 0
total = 0
nums = []
n = int(input())
for _ in range(n):
    x = int(input())
    nums.append(x)
    total += x
    count[x]+= 1
    if count[x] > most:
        most = count[x]

mostest = []
for k,v in count.items():
    if v == most:
        mostest.append(k)

nums.sort()
mostest.sort()
mid = n//2
print(round(total/n))
print(nums[mid])
if len(mostest) == 1:
    print(mostest[0])
else:
    print(mostest[1])
print(nums[-1] - nums[0])




