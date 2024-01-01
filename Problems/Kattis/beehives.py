import math
while True:
    d, numhives = list(map(float, input().split()))
    if d == 0 and numhives ==0: break
    hives = {}

    def distance(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    for i in range(int(numhives)):
        x , y = list(map(float, input().split()))
        hives[str(i)] = [x,y, False]


    for shive, slocation in hives.items():
        sx = slocation[0]
        sy = slocation[1]
        ssour = slocation[2]

        for ehive, elocation in hives.items():
            ex = elocation[0]
            ey= elocation[1]
            esour = elocation[2]

            if ex == sx and ey == sy: continue
            else:
                if distance(sx,sy,ex,ey) <= d:
                    hives[ehive][2] = True
                    hives[shive][2] = True
    
    sour = 0
    sweet = 0
    for data in hives.values():
        if data[2] == True:
            sour += 1
        else:
            sweet += 1
    print(f"{sour} sour, {sweet} sweet")


