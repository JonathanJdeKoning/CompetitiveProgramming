from collections import deque
while True:
    layers, rows, cols = map(int, input().split())
    if layers==0 and rows==0 and cols==0: break
    start = None
    end = None

    dung = []
    for i in range(layers):
        layer = []
        for j in range(rows):
            row = list(input())
            if "S" in row: start = (i,j,row.index("S"))
            if "E" in row: end = (i,j,row.index("E"))
            layer.append(row)
        input()
        dung.append(layer)

    directions = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]
    q = deque([start])
    time = -1
    seen = set()
    found = False
    while q:
        time += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in seen: continue
            if curr == end:
                print(f"Escaped in {time} minute(s).")
                found = True
                break
            seen.add(curr)

            for dl, dy, dx in directions:
                l = curr[0]+dl
                y = curr[1]+dy
                x = curr[2]+dx

                if l<0 or y<0 or x<0 or l==layers or y==rows or x==cols or dung[l][y][x] =="#" or (l,y,x) in seen: continue
                
                q.append((l,y,x))
        if found: break
    if not found:
        print("Trapped!")


