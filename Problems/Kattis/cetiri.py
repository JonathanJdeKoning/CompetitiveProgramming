x,y,z = sorted(list(map(int, input().split())))

if y-x == z-y:
    print(z+(z-y))
elif y-x > z-y:
    print(y-(z-y))
elif z-y>y-x:
    print(z-(y-x))
