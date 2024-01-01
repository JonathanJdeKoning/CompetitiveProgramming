import math
numregions = int(input())
regions = sorted(list(map(int, input().split())))

neededregions = int(math.ceil(len(regions)/2))

totalvotes = sum(regions)

minny = 0
for i in range(neededregions):
    minny += int(math.ceil(regions[i]/2))

print(totalvotes-minny)
