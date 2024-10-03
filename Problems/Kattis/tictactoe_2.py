tc = int(input())
def solve():
    xs, os = 0, 0
    mat = []

    for _ in range(3):
        row = list(input())
        xs += row.count("X")
        os += row.count("O")
        mat.append(row)
    
    xWin, oWin = 0,0
    for row in mat:
        if row.count("X") == 3: xWin += 1
        if row.count("O") == 3: oWin += 1

    for i in range(3):
        col = [row[i] for row in mat]
        if col.count("X") == 3: xWin += 1
        if col.count("O") == 3: oWin += 1

    mainDiag = [mat[0][0], mat[1][1], mat[2][2]]
    offDiag = [mat[0][2], mat[1][1], mat[2][0]]
    if mainDiag.count("X") == 3: xWin += 1
    if mainDiag.count("O") == 3: oWin += 1
    if offDiag.count("X") == 3: xWin += 1
    if offDiag.count("O") == 3: oWin += 1

    if xs != os and xs != os+1: return "no"
    if xWin and oWin: return "no"
    if oWin and xs > os: return "no"
    if xWin and os == xs: return "no"

    return "yes"

for i in range(tc):
    print(solve())
    if i != tc-1:
        input()