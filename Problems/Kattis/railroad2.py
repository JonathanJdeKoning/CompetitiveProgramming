x, y = list(map(int, input().split()))

if (x*4+y*3) %2 == 0:
    print("possible")
else:
    print("impossible")
