n, k = map(int, input().split())
nums = list(map(int, input().split()))
possible = len(set(nums[k-1:]))==1
if not possible:
    print(-1)
else:
    total = 0
    for num in nums[::-1]:
        if num == nums[k-1]:
            total += 1
        else:
            break
    print(len(nums)-total)
