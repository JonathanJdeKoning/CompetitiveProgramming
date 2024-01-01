tests = int(input())

for i in range(tests):
    nums = list(map(int, input().split()))

    numslen = nums[0]
    nums = nums[1:]
    good = True
    
    for i in range(2,numslen):
        if nums[i] - nums[i-1] != nums[i-1] - nums[i-2]:
            good = False
    
    if good:
        print("arithmetic")
    else:
        good = True
        nums = sorted(nums)
        for i in range(2,numslen):
            if nums[i] - nums[i-1] != nums[i-1] - nums[i-2]:
                good = False
        if good: 
            print("permuted arithmetic")
        else:
            print("non-arithmetic")
