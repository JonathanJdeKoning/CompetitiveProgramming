# Part 1
nails = [10,19,15,14,17,15,7,15,19,12,12]
print(sum([x-min(nails) for x in nails]))

# Part 2
nails = []
with open("in/quest4pt2.in", "r") as file:
    for line in file.readlines():
        nails.append(int(line))
print(sum([x-min(nails) for x in nails]))

# Part 3
from math import inf
nails = []
with open("in/quest4pt3.in", "r") as file:
    for line in file.readlines():
        nails.append(int(line))

nails.sort()
ans = sum([abs(x - nails[len(nails)//2]) for x in nails])
print(ans)