out = []
def solve(arr):
    if not arr:
        return

    solve(arr[2:])
    out.append(arr[0])

n = int(input())
nums = input().split()
solve(nums)
print(" ".join([str(x) for x in out]))
