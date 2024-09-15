a,b,c,x,y,z = map(int, input().split())
if c < z:
    exit(print(1))
elif z < c:
    exit(print(2))
else:
    if b < y:
        exit(print(1))
    elif y < b:
        exit(print(2))
    else:
        if a < x:
            print(1)
        else:
            print(2)
