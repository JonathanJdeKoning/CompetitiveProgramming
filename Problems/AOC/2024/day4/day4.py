ans = 0
mat = []
with open("day4.in", "r") as file:
    for x in file.readlines():
        line = x.strip()
        mat.append(list(line))

directions = [(-1,-1), (-1,1),(1, -1), (1,1)]
R, C = len(mat), len(mat[0])
for i in range(R):
    for j in range(C):
        if mat[i][j] != "A":
            continue
        
        corns = []
        for dy, dx in directions:
            y = i+dy
            x = j+dx
            if min(y,x) == -1 or y==R or x==C: break
            corns.append(mat[y][x])
        else:
            ans += 1
    
print(ans)