from collections import deque
R, C, k = map(int, input().split())
cols = list(map(int, input().split()))

mat = [list(input()) for _ in range(R)]

s = []
for c in cols: 
    s.append((0,c))

while s:
    y, x = s.pop()
    mat[y][x] = "~"

    if y == R-1 or mat[y+1][x] == "~": continue
    
    down = mat[y+1][x]
    if down == "O":
        s.append((y+1, x))
    else:
        if x != C-1 and mat[y][x+1] == "O":
            s.append((y, x+1))
        if x != 0 and mat[y][x-1] == "O":
            s.append((y, x-1))
    
for row in mat:
    print("".join(row))



