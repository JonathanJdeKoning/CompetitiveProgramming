while True:
    n = int(input())
    if n ==0: break
    o = 0
    s = 0
    points = []
    for _ in range(n):
        x,y = map(int, input().split())
        points.append((x,y))
    mid = len(points)//2
    xA, yA = points[mid] 

    for x, y in points:
        if y==yA or x ==xA: continue

        if y>yA and x > xA:
            s+= 1
        if y < yA and x < xA:
            s += 1

        if x < xA and y > yA:
            o += 1
        if x > xA and y < yA:
            o += 1

    print(s, o)
