n, sX, sY, eX, eY = map(int, input().split())



d = {"S": (0, -1), "E": (1,0), "W": (-1,0), "N": (0, 1)}

s = input()
def dist(x, y):
    return abs(y-eY) + abs(x-eX)

for i,c in enumerate(s, start=1):
    dx, dy = d[c]
    tempX, tempY = sX+dx, sY+dy

    if dist(tempX, tempY) < dist(sX, sY):
        sX, sY = tempX, tempY
        if (sX, sY) == (eX, eY):
            print(i)
            break
else:
    print(-1)

