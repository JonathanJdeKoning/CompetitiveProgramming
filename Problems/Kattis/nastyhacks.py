cases = int(input())

for case in range(cases):
    r, e, c = list(map(int, input().split()))

    if r > e - c:
        print("do not advertise")
    elif r == e - c:
        print("does not matter")
    else: 
        print("advertise")