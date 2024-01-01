x1, y1 = list(map(int,input().split()))
x2, y2 = list(map(int,input().split()))
x3, y3 = list(map(int,input().split()))

xs = [x1,x2,x3]
ys = [y1,y2,y3]

outx = 0

for x in xs:
    if xs.count(x) == 1:
        outx = x

for y in ys:
    if ys.count(y) == 1:
        outy = y

print(f"{outx} {outy}")