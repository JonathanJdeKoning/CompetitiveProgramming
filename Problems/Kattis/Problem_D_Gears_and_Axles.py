from collections import defaultdict
from math import log


n = int(input())
gears = defaultdict(list)
for i in range(n):
    gear = list(map(int, input().split(' ')))
    gears[gear[0]].append(gear[1])

addition = 0
for x in gears:
    gears[x].sort()
    for gear in range(len(gears[x])//2):
        ratio = gears[x][len(gears[x]) - 1 - gear] / gears[x][gear]
        addition += log(ratio)

print(addition)