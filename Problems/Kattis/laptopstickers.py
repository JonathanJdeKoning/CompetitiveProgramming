C, R, N = map(int, input().split())
lap = [list("_"*C)for _ in range(R)]

for i in range(N):
    stick = chr(i+97)

    sLen, sHei, x,y = map(int, input().split())

    for i in range(y, y+sHei):
        for j in range(x, x+sLen):
            if i < R and j < C:
                lap[i][j] = stick

for row in lap:
    print("".join(row))
