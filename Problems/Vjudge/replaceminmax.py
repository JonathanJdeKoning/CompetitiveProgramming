n = int(input())
nums = list(map(int, input().split()))
mn = min(nums)
mx = max(nums)
mnx = nums.index(mn)
mxx = nums.index(mx)

nums[mxx] = mn
nums[mnx] = mx
print(" ".join([str(x) for x in nums]))
