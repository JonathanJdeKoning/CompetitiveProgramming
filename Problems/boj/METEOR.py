R, C = list(map(int, input().replace(","," ").split()))
mat = [list(input()) for _ in range( R )]
dist = float('inf')
for j in range(C):
    bottom = -9999999
    for i in range(R):
        if mat[i][j] == "X":
            bottom = i
        elif mat[i][j] == "#":
            dist = min(dist, abs(i-bottom)-1)
            break
new = [["."]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        cell = mat[i][j]
        if cell == "X":
            new[i+dist][j] = "X"
        elif cell == "#":
            new[i][j] = "#"
        else: continue
for row in new:
    print("".join(row)) 
