numnums = int(input())

nums = list(map(int, input().split()))
print(sum([max(nums)-x for x in nums]))
