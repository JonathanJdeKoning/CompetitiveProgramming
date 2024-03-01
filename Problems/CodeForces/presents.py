n  = int(input())
res = [None]* n

nums = list(map(int, input().split()))

for fromm, to in enumerate(nums):
    res[to-1] = fromm+1
print(" ".join([str(r) for r in res]))
