from collections import Counter
n=int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
mxDiff = nums[-1] - nums[0]
ways = 0
count = dict(Counter(nums))
if mxDiff != 0:
    for num in count.keys():
        ways += count[num]*count.get(num+mxDiff, 0)
else:
    n = len(nums)
    ways = (n*(n-1))//2
print(mxDiff, ways)
