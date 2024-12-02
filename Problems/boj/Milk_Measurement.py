ans = 0
N = int(input())
data  = []
mp = {}
for  _ in range(N):
    day, cow, change = input().split()
    day = int(day)
    change = int(change)
    data.append((day,cow,change))
    mp[cow] = 7
data.sort()
display = set(list(mp.keys()))
for day, cow, change in data:
    mp[cow] += change
    mx = max(list(mp.values()))
    newdisplay = set([k for k,v in mp.items() if v == mx])
    if newdisplay != display:
        ans += 1
        display = newdisplay

print(ans)
