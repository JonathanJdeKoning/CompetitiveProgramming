numnums, op = map(int, input().split())
nums = list(map(int, input().split()))
import math
from collections import Counter
if op == 1:
    found = False
    for i, num in enumerate(nums):
        if (7777 - num) in nums:
            print("Yes")
            found = True
            break
    if not found:
        print("No")
elif op == 2:
    if len(list(set(nums))) == len(nums):
        print("Unique")
    else:
        print("Contains duplicate")
elif op == 3:
    half = len(nums)/2
    count = dict(Counter(nums))
    found = False
    for k, v in count.items():
        if v > half:
            print(k)
            found = True
            break
    if not found: print(-1)
        
elif op == 4:
    nums = sorted(nums)
    mid = len(nums)//2
    if len(nums)%2 == 0:
        print(nums[mid-1], nums[mid])
    else:
        print(nums[mid])
    
    
elif op == 5:
    print(" ".join(sorted([str(x) for x in nums if x >=100 and x <= 999])))
    
