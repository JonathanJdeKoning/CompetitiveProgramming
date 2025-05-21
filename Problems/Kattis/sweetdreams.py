from math import dist

x, y = list(map(int, input().replace(","," ").split()))
N = int(input())
for _ in range(N):
    a,b = list(map(int, input().replace(","," ").split()))
    if dist((x,y), (a,b)) <= 8:
        exit(print("NO"))
print("YES")