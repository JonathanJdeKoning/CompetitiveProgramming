from collections import defaultdict
N = int(input())
points = []
xs = defaultdict(int)
ys = defaultdict(int)

for _ in range(N):
    x,y = map(int, input().split())
    xs[x] += 1
    ys[y] += 1
    points.append((y,x))

ans = 0

for y,x in points:
    ans += (ys[y]-1) * (xs[x]-1)
print(ans)