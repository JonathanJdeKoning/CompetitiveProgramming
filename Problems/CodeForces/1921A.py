for tc in range(int(input())):
    points = [list(map(int, input().replace(","," ").split())) for _ in range(4)]
    xs = set([point[0] for point in points])
    ys = set([point[1] for point in points])

    print(abs(xs.pop() - xs.pop()) * abs(ys.pop() - ys.pop()))
    