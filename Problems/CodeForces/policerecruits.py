numevents = int(input())
police = 0
free = 0
nums = list(map(int, input().split()))
for num in nums:
    if num == -1:
        if police > 0 :
            police -= 1
        else:
            free += 1
    else:
        police += num
print(free)
