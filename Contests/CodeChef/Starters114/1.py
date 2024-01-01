tc = int(input())

for _ in range(tc):
    x,y,z = list(map(int, input().split()))

    wall = x*y
    paint = z/2
    import math
    print(int(math.floor(paint/wall)))
