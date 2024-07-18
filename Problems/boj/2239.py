mat = []
for _ in range(9):
    mat.append(list(map(int,list(input()))))

def possible(y,x):
    good = {1,2,3,4,5,6,7,8,9}
    good -= set(mat[y])
    good -= set([row[x] for row in mat])
    ySec,xSec = 3*(y//3), 3*(x//3)
    quad = [row[xSec:xSec+3] for row in mat[ySec:ySec+3]]
    for row in quad: good -= set(row)
    return good



def dfs(y,x):
    print(y,x)
    if y==9: return

    if mat[y][x]!=0:
        if x==8: dfs(y+1,0)
        else:
            dfs(y,x+1)
    poss = possible(y,x)
    if not poss: return
    for p in poss:
        mat[y][x] = p
        if x==8: dfs(y+1,0)
        else: dfs(y,x+1)
    mat[y][x] = 0



dfs(0,0)
for row in mat:
    print(row)
