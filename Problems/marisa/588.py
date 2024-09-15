x,y =map(int, input().split())
ans = 0
currDay = x
if currDay not in [8,7]: ans += 1
for i in range(y-1):
    currDay += 1
    if currDay == 9: currDay = 2
    if currDay not in [8,7]:
        ans += 1


print(ans)
