n, k = map(int, input().split())
nums = [input() for _ in range(n)]
ans = 0

for num in nums:
    for i in range(k+1):
        if str(i) not in num:
            break
    else:
        ans += 1
    continue

print(ans)
