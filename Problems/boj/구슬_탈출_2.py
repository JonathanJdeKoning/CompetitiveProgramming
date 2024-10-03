from math import inf
R,C = list(map(int, input().split()))
mat = []
redY,redX = None,None
blueY,blueX = None,None
goalY, goalX = None, None
for i in range(R):
    row = list(input())
    if "R" in row:  redY,  redX = i, row.index("R")
    if "B" in row: blueY, blueX = i, row.index("B")
    if "O" in row: goalY, goalX = i, row.index("O")
    mat.append(row)

directions = [(0,-1),(1,0),(0,1),(-1,0)]
mn = inf
def dfs(redY, redX, blueY, blueX, turns):
    global mn
    if turns == 10: return

    oldRedY, oldRedX, oldBlueY, oldBlueX = redY, redX, blueY, blueX
    for dy, dx in directions:
        good = False
        bad = False
        stagnant = False
        redY,   redX =  oldRedY,  oldRedX
        blueY, blueX = oldBlueY, oldBlueX
        while not stagnant:
            stagnant = True
            newRedY ,  newRedX =  redY+dy, redX +dx
            newBlueY, newBlueX = blueY+dy, blueX+dx

            if mat[newRedY][newRedX] == "O" or (mat[newRedY][newRedX] != "#" and (newRedY, newRedX) != (blueY, blueX)):
                redY = newRedY
                redX = newRedX
                stagnant = False
            elif (newRedY, newRedX) == (blueY, blueX):
                if mat[newRedY + dy][newRedX + dx] == ".":
                    redY = newRedY
                    redX = newRedX
                    stagnant = False

            if mat[newBlueY][newBlueX] == "O" or (mat[newBlueY][newBlueX] != "#" and (newBlueY, newBlueX) != (redY, redX)):
                blueY = newBlueY
                blueX = newBlueX
                stagnant = False
            elif (newBlueY, newBlueX) == (redY, redX):
                if mat[newBlueY + dy][newBlueX + dx] == ".":
                    blueY = newBlueY
                    blueX = newBlueX
                    stagnant = False
            
            if blueY==goalY and blueX==goalX:
                good = False
                bad = True
                continue
            if redY==goalY and redX==goalX:
                good = True

        if good and not bad: mn = min(mn, turns+1)
        if oldRedY == redY and oldRedX == redX and oldBlueY == blueY and oldBlueX == blueX: continue
        if not bad: dfs(redY, redX, blueY, blueX, turns+1)

dfs(redY, redX, blueY, blueX, 0)

if mn == inf:
    print(-1)
else:
    print(mn)
