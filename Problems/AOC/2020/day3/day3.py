from functools import reduce
with open("day3.in", "r") as file:
    mat = []
    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    for line in file.readlines():
        mat.append(list(line))
    out = []
    for slopeY, slopeX in slopes:
        ans = 0
        y = 0
        x = 0
        while True:
            try:
                v = mat[y][x]
                if v== "#": ans += 1
                y += slopeY
                x += slopeX
                x = x%(len(mat[0])-1)

            except:
                out.append(ans)
                break
    print(out[1])
    print(reduce(lambda a,b: a*b, out))