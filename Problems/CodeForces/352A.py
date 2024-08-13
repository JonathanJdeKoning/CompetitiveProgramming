n = int(input())
nums = list(map(int, input().split()))

fives = nums.count(5)
zeros = nums.count(0)
if zeros == 0:exit(print(-1))

usable = 0
curr = 0
for i in range(fives):
    curr+=5
    if curr%9==0:
        usable = i+1
if usable == 0:exit(print(0))

print(f"{usable*'5'}{zeros*'0'}")
