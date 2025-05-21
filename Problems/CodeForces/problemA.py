# Created by Jonathan de Koning on 2024-12-21 [>_]
from math import sqrt
N = int(input())
x = list(map(int, input().replace(","," ").split()))
y = list(map(int, input().replace(","," ").split()))
points = list(zip(x, y))
mx = 0
for i in range(len(points)-1):
    ax, ay = points[i]
    for j in range(i+1, len(points)):
        bx, by = points[j]
        mx = max(mx, abs(ay-by)**2 + abs(ax-bx)**2)
print(mx)