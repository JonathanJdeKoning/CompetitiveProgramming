from collections import deque

R, C = map(int, input().split())
mat = []
init = []
for i in range(R):
    row = list(input())
    for j, cell in enumerate(row):
        if cell == "V": init.append((i,j))
    mat.append(row)

q = deque(init)
seen = set()
lnr = [(0,1),(0,-1)]
while q:
    for _ in range(len(q)):
        curr = q.popleft()
        currY, currX = curr
        if curr in seen or currY == R-1: continue
        seen.add(curr)
        under = mat[currY+1][currX]
        if under == ".":
            mat[currY+1][currX] = "V"
            q.append((currY+1, currX))
        elif under == "#":
            for dy, dx in lnr:
                y = currY + dy
                x = currX + dx

                if x != -1 and x != C and mat[y][x]!="#":
                    mat[y][x] = "V"
                    q.append((y,x))
for row in mat:
    print("".join(row))



