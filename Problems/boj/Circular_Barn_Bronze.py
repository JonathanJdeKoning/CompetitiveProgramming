from math import inf
rooms = [int(input()) for _ in range(int(input()))]
best = inf
for i in range(len(rooms)):
    ans = 0
    start = i
    for room in range(i, len(rooms)+i):
        dist = room - i
        roomsize = rooms[room%len(rooms)]
        ans += dist*roomsize
    best = min(best, ans)

print(best)