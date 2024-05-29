for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    out = []
    for i in range(len(nums)+1):
        for j in range(i+1, len(nums)+1):
            out.append(str(max(nums[i:j])))
    print(" ".join(out))
