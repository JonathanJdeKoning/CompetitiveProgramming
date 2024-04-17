import math
for _ in range(int(input())):
    a,b = map(int, input().split())
    dist = abs(b-a)
    print(math.ceil(dist/10))
