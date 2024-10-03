N = int(input())
mx = 0
houses = []
spies = []
for i in range(N):
    row = list(input())
    for j in range(N):
        if row[j] == "S": spies.append((i,j))
        elif row[j] == "H": houses.append((i,j))

from math import inf
for spyY, spyX in spies:
    mn = inf
    for houseY, houseX in houses:
        mn = min(mn, abs(spyY-houseY)+abs(spyX-houseX))
    mx = max(mx, mn)
print(mx) 