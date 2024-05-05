n = int(input())
nums = list(map(int, input().split()))

mx = 1
start = nums[0]
run = 1
for num in nums[1:]:
    if num >= start:
        run += 1
        mx = max(mx, run)
    else:
        run = 1
    start = num
print(mx)
