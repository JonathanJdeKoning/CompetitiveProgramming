while True:
    a,b = map(int, input().split())
    if min(a,b)<1: break
    nums = list(range(min(a,b), max(a,b)+1))
    print(" ".join([str(x) for x in nums]), end="")
    print(f" sum ={sum(nums)}")
