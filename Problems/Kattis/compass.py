start = int(input())
end = int(input())


oneway = 0
onestart = start
while True:
    if onestart == 360:
        onestart = 0
    if (onestart == 0 or onestart == 360) and (end == 0 or end == 360):
        break
    oneway += 1
    onestart+=1
    if onestart == end:
        break
    elif onestart == 360:
        onestart = 0
    if onestart == end:
        break

otherway = 0
otherstart = start
while True:
    if otherstart == 0:
        otherstart = 360
    if (otherstart == 0 or otherstart == 360) and (end ==0 or end == 360):
        break
    otherway-=1
    otherstart-=1
    if otherstart == end:
        break
    elif otherstart == 0:
        otherstart = 360
    if otherstart == end:
        break
if start==end:
    print(0)
elif abs(oneway) < abs(otherway):
    print(oneway)
elif abs(otherway) < abs(oneway):
    print(otherway)
elif abs(oneway) == abs(otherway):
    print(oneway)
