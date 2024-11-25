nums = [list(map(int, input().split())) for _ in range(11)]

nums.sort()

pen = 0
curr = 0
for time, wrong in nums:
    curr += time
    pen += curr
    pen += wrong*20

print(pen)
