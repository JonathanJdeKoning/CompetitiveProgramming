from itertools import groupby

N = int(input())
A = list(map(int, input().replace(","," ").split()))

winters =[]
days = set()
mx = 0
idx = 0
for k, v in groupby(A, key=lambda x: x<0):
    l = len(period := list(v))
    idx += l
    if period[0] >= 0 : continue
    
    mx = max(mx, l)
    winters.append((idx-l, l))

mxs = [winter for winter in winters if winter[1] == mx]

for start, length in winters:
    for i in range(start-1, max(-1, (start-length*2)-1), -1):
        days.add(i)

best = 0
for start, l in mxs:
    add = 0
    for i in range(start-1, max(-1, (start-l*3)-1), -1):
        if i not in days:
            add += 1
    best = max(best, add)


print(len(days)+best)