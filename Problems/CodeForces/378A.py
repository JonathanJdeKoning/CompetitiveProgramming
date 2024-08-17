a,b = map(int, input().split())

awin = 0
draw = 0
bwin = 0

for i in range(1,7):
    if abs(a-i) < abs(b-i):
        awin += 1
    elif abs(b-i) < abs(a-i):
        bwin += 1
    else:
        draw += 1
print(awin, draw, bwin)
