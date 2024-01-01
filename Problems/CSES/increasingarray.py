n = int(input())
nums = list(map(int, input().split()))

total = 0

prev = nums[0]
for i in nums[1:]:
    if i < prev:
        total += prev-i
        continue
    prev = i
print(total)
