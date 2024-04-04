first = True
while True:
    rows = int(input())
    if rows == 0: break
    if first:
        first = False
    else:
        print()
    mat = []
    mxlen = 0
    for _ in range(rows):
        row = list(input())
        new = []
        for c in row:
            if c == "-":
                new.append("|")
            elif c == "|":
                new.append("-")
            else:
                new.append(c)
        mxlen = max(mxlen, len(row))
        mat.append(new)
    for i in range(len(mat)):
        for j in range(mxlen-len(mat[i])):
            mat[i].append(" ")

    mat = list(zip(*mat[::-1]))

    for row in mat:
        line = "".join(row)
        line = line.rstrip()
        print(line)
