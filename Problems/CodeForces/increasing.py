def solve():
    input()
    nums = sorted(list(map(int, input().split())))
    start = nums[0]
    for num in nums[1:]:
        if num <= start:
            return "NO"
        start = num
    return "YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve())
