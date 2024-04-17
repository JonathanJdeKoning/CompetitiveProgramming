for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    arr = sorted(nums[:])
    mx,sec = arr[-1],arr[-2]

    out = []
    for num in nums:
        if num != mx:
            out.append(num-mx)
        else:
            out.append(mx-sec)
    print(" ".join([str(x) for x in out]))
