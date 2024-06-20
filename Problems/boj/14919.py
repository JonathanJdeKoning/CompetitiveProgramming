import sys
input = sys.stdin.readline

m = int(input())
ans = [0]*m
nums = sorted(list(map(float, input().split())))

currBucket = 0
currVal = (currBucket+1)*(1/m)
currVal = float(str(currVal)[:10])
for i, num in enumerate(nums):
    if num < currVal:
        ans[currBucket] += 1
    else:
        while num >= currVal:
            currBucket += 1
            currVal += (1/m)
            currVal = float(str(currVal)[:10])
        ans[currBucket] += 1

print(" ".join(map(str, ans)))


