input()
nums = set(map(int, input().split()))
input()
for x in list(map(int, input().split())):
    if x in nums:
        print(1)
    else:
        print(0)
