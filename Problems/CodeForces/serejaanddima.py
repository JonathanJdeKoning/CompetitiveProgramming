from collections import deque
numnums = int(input())

nums = list(map(int, input().split()))

a = 0
b = 0

c = 0
while nums:
    c+=1
    if nums[0] > nums[-1]:
        if c%2==1:
            a += nums[0]
        else:
            b += nums[0]
        nums = nums[1:]
    else:
        if c%2 ==1:
            a += nums[-1]
        else:
            b+= nums[-1]
        nums = nums[:-1]
print(a,b)
