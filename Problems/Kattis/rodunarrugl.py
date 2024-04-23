n = int(input())
nums = list(map(int, input().split()))

bad = 0

for i, num in enumerate(nums):
    if num != i+1:
        bad += 1

total = bad+1
if bad == n:
    total += 2
if bad == 0:
    total -=1
print(total)
