n = input()
nums = list(map(int, input().split()))
def rep(x):
    if x < 0:
        return 2
    elif x > 0:
        return 1
    return 0
nums = list(map(rep, nums))
print(" ".join([str(x) for x in nums]))
