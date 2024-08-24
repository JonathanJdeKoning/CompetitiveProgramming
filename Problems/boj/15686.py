n,k = map(int, input().split())
mat = []
homes = []
chicken = []
for i in range(n):
    row = map(int, input().split())
    for j, cell in enumerate(row):
        if cell == 1:
            homes.append((i,j))
        elif cell == 2:
            chicken.append((i,j))

from itertools import combinations
combs = combinations(chicken, k)
from math import inf

ans = inf

for comb in combs:
    combMN = 0
    for homeY,homeX in homes:
        homeMN = inf
        for cY, cX in comb:
            homeMN = min(homeMN, abs(homeY-cY)+abs(cX-homeX))
        combMN += homeMN
    ans = min(ans, combMN)
print(ans)
