from bisect import bisect_left
nums = [0]
ans = 0
for i in range(1, 999999+1):
    s = str(i)
    if s.count("0") == len(s)-1:
        ans += 1
    nums.append(ans)


for tc in range(int(input())):
    N = int(input())
    print(nums[N])