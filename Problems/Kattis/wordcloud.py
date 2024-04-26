from math import ceil
cloud = 1
while True:
    total = 0
    w, n = map(int, input().split())
    if (w,n) == (0,0): break
    d = {}
    pointsize = {}
    width = {}
    mx = 0
    for _ in range(n):
        s, cnt = input().split()
        cnt = int(cnt)
        if cnt < 5: continue
        d[s] = cnt
        mx = max(mx, cnt)

    for word, count in d.items():
        pointsize[word] = 8+ceil((40*(count-4))/(mx-4))
        width[word] = ceil((9.0/16.0)*len(word)*pointsize[word])

    rowTotal = 0
    maxHeight = 0
    for word, wid in width.items():
        if wid + rowTotal > w:
            total += maxHeight
            maxHeight = pointsize[word]
            rowTotal = wid+10
        else:
            rowTotal += wid+10
            maxHeight = max(maxHeight, pointsize[word])
    total += maxHeight

    #print(pointsize)
    #print(width)
    print(f"CLOUD {cloud}: {total}")
    cloud += 1
