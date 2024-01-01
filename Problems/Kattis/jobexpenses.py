nums = int(input())

numList = list(map(int, input().split()))

total = 0
for num in numList:
    if num < 0:
        total += abs(num)
print(total)