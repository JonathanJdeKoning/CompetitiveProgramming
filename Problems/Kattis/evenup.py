
def solve():
    numnums = int(input())
    if numnums == 1: return 1
    nums = list(map(int,input().split()))
    stack = [nums[0],nums[1]]

    currnum = 1

    while currnum != (numnums):
        new = nums[currnum]
        sec = stack.pop()

        if new%2 == sec%2:
            stack.append(2)
        else:
            stack.append(sec)
            stack.append(new)
        currnum += 1
    return len(stack)



print(solve())
