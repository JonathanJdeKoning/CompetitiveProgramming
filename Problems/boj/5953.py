n = int(input())
nums = [int(input()) for _ in range(n)]

for i, num in enumerate(nums[1:], start=1):
    nums[i] = max(num, num+nums[i-1])
print(max(nums))
