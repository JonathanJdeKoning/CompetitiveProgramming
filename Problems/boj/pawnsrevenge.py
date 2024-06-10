def solve():
    def ok(y,x):
        return y!=-1 and x!=-1 and y!=n and x!=n


    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(input()))

    total = 0
    king = set()
    bad = set()
    kingDirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            if cell == "-": continue
            if cell == "K":
                for dy, dx in kingDirs:
                    y = i+dy
                    x = j+dx

                    if not ok(y,x): continue
                    king.add((y,x))
                continue
            if i==n-1: return-1
            bad.add((i,j))

    accounted = set()
    for pos in king:
        bad.discard(pos)
        accounted.add(pos)
    doubles = 0
    for pawnY, pawnX in bad:
        if (pawnY, pawnX) in accounted: continue
        total += 1
        accounted.add((pawnY, pawnX))
        # Get possible spots
        left = (pawnY+1, pawnX-1) if pawnX != 0 else None
        right = (pawnY+1, pawnX+1) if pawnX != n-1 else None
        poss = {x for x in [left, right] if x}

        if left and mat[left[0]][left[1]] == "*": poss.discard(left)
        if right and mat[right[0]][right[1]] == "*" : poss.discard(right)

        if not poss: return -1

        if len(poss) == 1:
            attacker = list(poss).pop()
            if pawnX == 0 and mat[pawnY][pawnX+2] == "*":
                if (pawnY, pawnX+2) not in accounted and mat[attacker[0]][attacker[1]] != "*":
                    accounted.add((pawnY,pawnX+2)) 
            if pawnX == n-1 and mat[pawnY][pawnX-2] == "*":
                if (pawnY, pawnX-2) not in accounted and mat[attacker[0]][attacker[1]]!= "*":
                    accounted.add((pawnY, pawnX-2))
            continue


        if pawnX < n-2 and mat[pawnY][pawnX+2] == "*":
            if (pawnY, pawnX+2) not in accounted:
                accounted.add((pawnY, pawnX+2))
                continue
            
        if pawnX > 0 and mat[pawnY][pawnX-2] == "*":
            if (pawnY, pawnX-2) not in accounted:
                accounted.add((pawnY, pawnX-2))
                continue
    return total

print(solve())

