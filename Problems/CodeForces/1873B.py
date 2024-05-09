for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    nums[0]+=1
    total = 1
    for num in nums:
        total*=num
    print(total)

