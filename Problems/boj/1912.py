n = int(input())
nums = [0]+list(map(int, input().split()))

for i in range(1,len(nums)):
    nums[i] = max(nums[i], nums[i]+nums[i-1])
print(max(nums[1:]))

