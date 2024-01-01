while True:
    lines = int(input())
    if lines == -1: break
    total = 0
    totalhours = 0
    for test in range(lines):
        logline = list(map(int, input().split()))
        speed = logline[0]
        hours = logline[1]
        total += speed*(hours-totalhours)
        totalhours = hours
    print(f"{total} miles")
