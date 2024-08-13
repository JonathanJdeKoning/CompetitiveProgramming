from collections import Counter
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    mx = 0
    total = 0
    ans = 0
    for num in nums:
        total += num
        if num > mx:
            total += mx
            mx = num
            total -= mx
        if total == mx:
            ans += 1
    print(ans)

        
