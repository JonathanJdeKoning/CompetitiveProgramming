sx, sy = list(map(int, input().replace(","," ").split()))
ex,ey = list(map(int, input().replace(","," ").split()))


xDist = abs(sx - ex)
yDist = abs(sy - ey)

print(max(xDist, yDist))