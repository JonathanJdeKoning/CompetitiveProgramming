def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    new = [nums[-1]]
    new.extend(nums[:-1])
    return " ".join(map(str, new))
for _ in range(int(input())):
    print(solve())
