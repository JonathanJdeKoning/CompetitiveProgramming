from itertools import accumulate
nums = [int(input()) for _ in range(10)]
A = list(accumulate(nums))
best = 0
for num in A:
    diff = abs(100-num)
    if diff <= abs(best-100):
        best = max(num, best)
print(best)

