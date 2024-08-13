for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    if nums.count(max(nums))%2==0:
        print("NO")
    else:
        print("YES")
