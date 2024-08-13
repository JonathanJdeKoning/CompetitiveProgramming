from itertools import takewhile
nums = [1,1,2,3,4,2,6,8,10,11,13,15,1,4]

print(list(takewhile(lambda x: x < 10, nums)))
print(nums)
