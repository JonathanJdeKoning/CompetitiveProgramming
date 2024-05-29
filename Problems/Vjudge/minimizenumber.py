n = int(input())
nums = list(map(int, input().split()))
total = 0
while len([x for x in nums if x%2==1]) == 0:
    nums = list(map(lambda x:x//2, nums))
    total += 1
print(total)
