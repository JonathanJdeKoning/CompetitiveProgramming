for _ in range(int(input())):
    n = int(input())
    mn = 999999999999
    nums = list(map(int, input().split()))
    for i, x, in enumerate(nums, start=1):
        for j, y in enumerate(nums[i:], start=i+1):
            mn = min(mn, x+y+j-i)
    print(mn)

