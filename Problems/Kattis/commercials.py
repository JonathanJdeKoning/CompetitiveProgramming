n, p = list(map(int, input().split()))
breaks = [x-p for x in list(map(int, input().split()))]
#[-2, 15, -14, 60, -5, 1]
import math
globalmax=breaks[0]
prevmax = breaks[0]

for x in breaks[1:]:
    if prevmax+x >= x:
        prevmax = prevmax+x
    if prevmax+x <= x:
        prevmax = x

    if prevmax > globalmax:
        globalmax = prevmax
print(globalmax)
    


