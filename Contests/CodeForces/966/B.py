def solve():
    n = int(input())
    nums = list(map(lambda x: int(x)-1, input().split()))
    sat = [0]*n
    sat[nums[0]] = 1

    for num in nums[1:]:
        if num == 0:
            if sat[1]:
                sat[0] = 1
            else:
                return "NO"
        elif num == n-1:
            if sat[-2]:
                sat[n-1] = 1
            else:
                return "NO"
        else:
            if sat[num+1] or sat[num-1]:
                sat[num] = 1
            else:
                return "NO"
    return "YES"

for _ in range(int(input())):
    print(solve())
