nums = list(map(int, input().split()))

print(sum([x**2 for x in nums])%10)
