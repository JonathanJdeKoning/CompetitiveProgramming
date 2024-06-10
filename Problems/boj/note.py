nums = list(map(int, input().split()))
if nums == sorted(nums):
    print("ascending")
elif nums == sorted(nums, reverse=True):
    print("descending")
else:
    print("mixed")
