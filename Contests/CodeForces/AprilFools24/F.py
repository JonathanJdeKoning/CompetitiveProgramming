mat = []
for i in range(21):
    line = input()
    mat.append(line)

mx = 0
for i in range(18):
    for j in range(18):
        tot = 0
        pos = 0
        for k in range(4):
            for l in range(4):
                pos += 1
                tot += int(mat[i+k][j+l])
        #print(pos)
        mx = max(mx, tot)
print(mx)

        

