nums = sorted(map(int, input().split()))
a = nums[0]
b = nums[1]
nums[nums.index(a+b)] = 999999999999
c = min(nums[2:])
print(a,b,c)