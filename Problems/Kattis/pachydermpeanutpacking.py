while True:
    numboxes = int(input())
    boxes = []
    if numboxes == 0: break
    
    for _ in range(numboxes):
        data = input().split()
        x1,y1,x2,y2 = map(float, data[:-1])
        size = data[-1]
        boxes.append((x1,y1,x2,y2, size))
    numpeanuts = int(input())
    for _ in range(numpeanuts):
        data = input().split()
        size = data[-1]
        x,y = map(float, data[:-1])
        bad = True
        for box in boxes:
            
            x1,y1,x2,y2 = box[:-1]
            boxsize = box[-1]
            if (x1<=x<=x2) and (y1<=y<=y2):
                if boxsize == size:
                    print(size, "correct")
                    bad = False
                else:
                    print(size, boxsize)
                    bad = False
        if bad:
            print(size, "floor")


    print()
