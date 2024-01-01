numstudents = int(input())
colors = list(map(int, input().split()))

from collections import Counter
count= Counter(colors)
tot = 0
for color in count.keys():
    tot+= int(color) + 1
print(tot)
