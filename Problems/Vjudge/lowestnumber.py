n = input()
nums = list(map(int, input().split()))
print(min(nums), 1+nums.index(min(nums)))
