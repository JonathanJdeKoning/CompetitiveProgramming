points = []
for _ in range(int(input())):
    points.append(tuple(map(int, input().split())))
points.sort(key=lambda x:(x[1],[x[0]]))
for a,b in points: print(a,b)

