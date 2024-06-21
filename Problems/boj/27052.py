used = set()
used.add((0,0,0))
pos = {1:(0,0,0)}
for curr in range(2,int(input())+1):
    dadBale, op = input().split()
    dadBale = int(dadBale)
    currH, currY, currX = pos[dadBale]
    
    if   op == "O": currH -= 1
    elif op == "U": currH += 1
    elif op == "B": currY -= 1
    elif op == "F": currY += 1
    elif op == "L": currX -= 1
    elif op == "R" :currX += 1

    if (currH, currY, currX) in used: print(-1);break
    used.add((currH, currY, currX))
    pos[curr] = (currH, currY, currX)
else:
    directions,ans = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)], 0
    for currH, currY, currX in used:
        total = 6 if currH != 0 else 5
        for dh, dy, dx in directions:
            if (currH+dh,currY+dy,currX+dx) in used: total -= 1
        ans += total
    print(ans)
