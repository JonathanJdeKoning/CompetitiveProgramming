x1,y1,x2,y2 = map(int, input().split())

xdist = abs(x1-x2)
ydist = abs(y1-y2)

if xdist and ydist and xdist != ydist:
    exit(print(-1))

if not xdist:
   exit(print(x1+ydist, y1, x1+ydist, y2))
if not ydist:
    exit(print(x1,y1+xdist,x2,y1+xdist))

print(x1,y2,x2,y1)


