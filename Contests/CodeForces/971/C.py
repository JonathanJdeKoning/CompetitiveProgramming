from math import ceil, floor
def solve():
    x,y,k= map(int, input().split())
    xM = ceil(x/k)
    yM = ceil(y/k)

    ans = max(xM, yM)*2

    if yM >= xM:
        ans += 1
    return ans -1


for _ in range(int(input())):
    print(solve())
