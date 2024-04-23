while True:
    try:
        nums = list(map(int, input().split()))[1:]
        n = len(nums)
        
        diffs = []
        start = nums[0]
        for num in nums[1:]:
            diffs.append(abs(num-start))
            start = num
        if sorted(diffs) == list(range(1,n)):
            print("Jolly")
        else:
            print("Not jolly")
        
    except EOFError:
        break
