def solve():
    sx, sy, ex, ey = list(map(int, input().replace(","," ").split()))    
    if ey < sy:
        return -1
    ans = 0
    ydist = ey - sy
    ans += ydist
    sy += ydist
    sx += ydist
    xdist = sx - ex
    if xdist < 0: return -1
    return ans + xdist



for tc in range(int(input())):
    print(solve())
   