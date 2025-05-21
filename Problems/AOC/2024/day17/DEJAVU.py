from collections import defaultdict
n = int(input())
points = set()
xs = defaultdict(int)
ans = 0
for _ in range(n):
    x,y = map(int, input().split())
    points.add((x,y))
    xs[x]+=1

for k, v in xs.items():
    if v == 2:
        ans += len(points)-2

for x,y in points:
    if (x+1,y^1) in points and (x+2, y) in points:
        ans+= 1

print(ans)

