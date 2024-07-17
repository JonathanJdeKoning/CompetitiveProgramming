from itertools import pairwise
while True:
    nums = list(map(int, input().split()))
    if nums == [0]: break
    nums = nums[1:]
    n = 1
    l = len(nums)

    while n != l:
        sms = nums[:n]
        dfs = nums[n:n*2]

        new = []

        for sm, df in zip(sms, dfs):
            a = (sm+df)//2
            b = sm-a
            if a-b == df:
                new.extend([a,b])
            elif b-a ==df: new.extend([b,a])
        new.extend(nums[n*2:])
        nums = new[:]
        n*=2
    print(" ".join(map(str,nums)))
             




