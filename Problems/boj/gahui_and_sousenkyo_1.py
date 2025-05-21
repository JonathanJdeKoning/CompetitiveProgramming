nums = list(map(int, input().replace(","," ").split()))
base = nums[0]
ans = len([x for x in nums[1:] if abs(x-base) <= 1000])
print(ans)