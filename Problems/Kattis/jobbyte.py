N = int(input())
nums = list(map(int, input().replace(","," ").split()))
nums = [x-1 for x in nums]
pos = {nums[i]:i for i in range(len(nums))}


ans = 0
corr = list(range(N))
for i, (a,b) in enumerate(zip(nums, corr)):
    if a == b: continue
    j = pos[b]
    nums[j], nums[i] = nums[i], nums[j]
    pos[nums[i]], pos[nums[j]] = pos[nums[j]], pos[nums[i]]
    ans += 1
print(ans)
