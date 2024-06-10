n,x = map(int, input().split())

nums = list(map(int, input().split()))

print(" ".join(map(str, [z for z in nums if z < x])))

