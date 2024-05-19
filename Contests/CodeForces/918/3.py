tc = int(input())
for _ in range(tc):
    numnums = int(input())
    nums = list(map(int, input().split()))
    summy = sum(nums)

    
    x = summy**0.5
    if x.is_integer():
        print("YES")
    else:
        print("NO")
