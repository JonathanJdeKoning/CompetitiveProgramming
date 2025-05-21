
def judgeBoard(s):
    s = s[::-1]
    b = [[None]*3 for _ in range(3)]
    for i in range(9):
        if s[i] == "0": continue
        r,c = divmod(i,3)
        if s[i+9] == "1": b[r][c] = "X"
        else: b[r][c] = "O"

    xwin = ["X", "X", "X"]
    owin = ["O", "O", "O"]
    for row in b:
        if row == xwin: return "X wins"
        if row == owin: return "O wins"

    for j in range(3):
        col = [row[j] for row in b]
        if col == xwin: return "X wins"
        if col == owin: return "O wins"

    md = [b[0][0], b[1][1], b[2][2]]
    sd = [b[0][2], b[1][1], b[2][0]]

    if md == xwin or sd == xwin : return "X wins"
    if md  == owin or sd == owin: return "O wins"

    for row in b:
        if None in row: return "In progress"
    return "Cat's"

N = int(input())
for _ in range(N):
    s = int(input(),8)
    print(judgeBoard(bin(s)[2:].zfill(19)))


    