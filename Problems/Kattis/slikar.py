from collections import deque
directions = [(-1,0),(0,-1),(1,0),(0,1)]
R, C = map(int, input().split())
water = deque([])
denY, denX = None, None
startY, startX = None, None
mat = []
for i in range(R):
    row = list(input())
    for j, cell in enumerate(row):
        if cell =="*":
            water.append((i,j))
        elif cell == "D":
            denY, denX = i,j
        elif cell == "S":
            startY, startX = i,j
    mat.append(row)

beav = deque([(startY, startX)])
seenbeav = set()
seenwater = set()
steps = -1
while beav or water:
    steps += 1
    for _ in range(len(water)):
        waterY, waterX = water.popleft()
        if (waterY, waterX) in seenwater: continue
        seenwater.add((waterY, waterX))

        for dy, dx in directions:
            y,x = dy+waterY, dx+waterX

            if min(y,x) == -1 or y==R or x==C or (y,x) in seenwater or mat[y][x] in  "XD": continue
            mat[y][x] = "*"
            water.append((y,x))
    #for row in mat: print("".join(row)) 
    #print()
    for _ in range(len(beav)):
        beavY, beavX = beav.popleft()
        if (beavY, beavX) in seenbeav: continue
        seenbeav.add((beavY, beavX))
        if (beavY, beavX) == (denY, denX): exit(print(steps))


        for dy, dx in directions:
            y,x = dy+beavY, dx+beavX

            if min(y,x) == -1 or y==R or x==C or (y,x) in seenbeav or mat[y][x] in "*X": continue
            beav.append((y,x))

print("KAKTUS")


