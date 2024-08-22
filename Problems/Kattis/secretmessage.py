for _ in range(int(input())):
    s = input()
    n = 0
    for i in range(100,-1,-1):
        if i**2 < len(s):
            n = i+1
            break

    mat = []
    for _ in range(n):
        mat.append(["*"]*n)

    curr = 0

    for i in range(n):
        for j in range(n):
            mat[i][j] = s[curr]
            curr += 1
            if curr == len(s):
                break
        else:
            continue
        break

    mat = list(zip(*mat[::-1]))
    out = []
    #for row in mat:
    #    print(row)
    for i in range(n):
        for j in range(n):
            cell = mat[i][j]
            if cell != "*":
                out.append(cell)
    print("".join(out))
