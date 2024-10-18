d, sumTime = list(map(int, input().split()))
days = []
currTime = 0
wowTime = 0
for i in range(d):
    mnTime, mxTime = list(map(int, input().split()))
    currTime += mnTime
    wowTime += mxTime
    days.append([mnTime, mxTime])

if currTime > sumTime or wowTime < sumTime: exit(print("NO"))

for i, (mn, mx) in enumerate(days):
    mxGain = mx-mn
    timeLeft = sumTime - currTime
    if mxGain < timeLeft:
        currTime += mxGain
        days[i][0] = mx
    else:
        days[i][0] += timeLeft
        break
print("YES")
print(" ".join(map(str, [mn for mn,mx in days])))


