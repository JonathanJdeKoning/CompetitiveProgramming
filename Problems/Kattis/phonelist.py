def solve():
    numnums = int(input())
    nums = sorted([input() for x in range(numnums)])
    for i, num in enumerate(nums[:-1]):
        if nums[i+1].startswith(num):
            return "NO"
    return "YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solve())
