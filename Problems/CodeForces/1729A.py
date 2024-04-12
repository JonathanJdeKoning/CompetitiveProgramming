for _ in range(int(input())):
    a,b,c = map(int, input().split())
    onedist = a-1
    twodist = abs(b-c) + abs(c-1)

    if onedist < twodist:
        print("1")
    elif twodist < onedist:
        print("2")
    else:
        print("3")
