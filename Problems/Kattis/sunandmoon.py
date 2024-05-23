prevSun, lenSun = map(int, input().split())
prevMoon, lenMoon = map(int, input().split())

sunGood = set()
good = set()
for i in range(0, 5001,lenSun):
    sunGood.add(i)
for i in range(0, 5001,lenMoon):
    if i in sunGood:
        good.add(i)
        if len(good) == 2:
            break
good = sorted(good)
print(good)
print(good[-1]-max(prevSun, prevMoon))

