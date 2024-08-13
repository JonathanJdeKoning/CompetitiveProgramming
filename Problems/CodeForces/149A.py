n = int(input())
nums = sorted(list(map(int, input().split())))

if sum(nums) < n:
    exit(print(-1))
tot = 0
ans = 0 
while tot < n:
    tot += nums.pop()
    ans += 1
print(ans)
