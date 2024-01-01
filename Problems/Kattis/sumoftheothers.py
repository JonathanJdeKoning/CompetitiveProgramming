while True:
    try:
        nums = list(map(int,input().split()))

        for num in nums:
            if num == sum(nums[:nums.index(num)] + nums[nums.index(num)+1:]):
                print(num)
                break
    except EOFError:
        break
