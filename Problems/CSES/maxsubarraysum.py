input()

nums = list(map(int, input().split()))
mx = nums[0] 
for i, num in enumerate(nums[1:], start = 1):
    best = max(num, nums[i-1]+num)
    if best > mx: mx = best
    nums[i] = best

print(mx)

