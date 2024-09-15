while True:
    mxW = int(input())
    if mxW == 0: break

    rects = []
    while True:
        rectW, rectH = map(int, input().split())
        if rectW == -1 and rectH == -1:
            break
        rects.append((rectW, rectH))

    roomW, roomH = 0,0
    currW, currH = 0,0

    for rectW, rectH in rects:
        if currW + rectW <= mxW:
            currW += rectW
            currH = max(currH, rectH)
            roomW = max(currW, roomW)
        else:
            roomH += currH
            currW = rectW
            roomW = max(roomW, currW)
            currH = rectH
    roomH+= currH
    print(f"{roomW} x {roomH}")


