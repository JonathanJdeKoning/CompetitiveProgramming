a,b,c,d = map(int, input().split())

aTime = []
bTime = []

while len(aTime) < 1002:
    aTime.extend([1]*a)
    aTime.extend([0]*b)

while len(bTime) < 1002:
    bTime.extend([1]*c)
    bTime.extend([0]*d)

for man in list(map(int, input().split())):
    y = man-1

    x = bTime[y] + aTime[y]

    if x == 1:
        print("one")
    elif x == 2:
        print("both")
    else:
        print("none")





