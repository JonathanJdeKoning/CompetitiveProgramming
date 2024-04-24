tc = int(input())
ns = []
from math import inf
while True:
    try:
        ns.extend(list(map(int, input().split())))
    except EOFError: break
getlen = True
getnum = False
countdown = 0
nums = []
length = None
for i, num in enumerate(ns):
    if getlen:
        nums = []
        length = num
        getlen = False
        getnum = True
    elif getnum:
        countdown = num
        getnum = False
    else:
        nums.append(num)
        countdown -= 1
        if countdown == 0:
            getlen = True
            getnum =  True
            nums = sorted(nums)
            mn = min(length-nums[0], nums[0])
            for ant in nums[1:]:
                mn = max(min(length-ant, ant),mn)
            print(mn,max(length-nums[0],nums[-1]))
            getlen = True             
