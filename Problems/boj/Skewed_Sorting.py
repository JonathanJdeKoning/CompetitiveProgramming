n = 2**int(input())
A = [int(input()) for _ in range(n)]
ans = 0
def mergeswap(nums):
    global ans
    if len(nums) != 2:
        mid = len(nums)//2
        left = mergeswap(nums[:mid])
        right = mergeswap(nums[mid:])

        if left[0] > right[0]:
            ans += len(nums)*len(left)
            nums = right + left
    else:
        if nums[0] > nums[1]:
            ans += 2
            nums = nums[::-1]
    return nums
nums = mergeswap(A)
print(ans)
print("\n".join(map(str, nums)))