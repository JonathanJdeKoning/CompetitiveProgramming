import math
bridges, knights, needed = list(map(int, input().split()))

groups = math.floor(knights/needed)
count = 0
while True:
    bridges -= groups
    count += 1
    if bridges <= 1:
        break
print(count)
