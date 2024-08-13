n= int(input())
nums = list(map(int, input().split()))
if nums.count(min(nums)) > 1:
    print("Still Rozdil")
else:
    print(nums.index(min(nums))+1)
