seen = set()
for i in range(int(input())):
    numnums = int(input())
    nums = list(map(int, input().split()))
    for num in set(nums):
        if nums.count(num) == 1:
            print(nums.index(num)+1)
        else:
            pass
