for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    total = 0
    for i in range(len(nums)+1):
        for j in range(i+1, len(nums)+1):
            slc = nums[i:j]
            if slc == sorted(slc):
                total += 1
    print(total)
