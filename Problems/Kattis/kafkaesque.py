n = int(input())
nums = [int(input()) for _ in range(n)]
loop = 0
curr = 0
done = False
while True:
    loop += 1
    for i in range(101):
        if i == nums[curr]:
            curr += 1
            if curr == len(nums):done = True;break
    if done: break
print(loop)
