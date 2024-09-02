R, C, k = map(int, input().split())
if k%2==1: exit(print("IMPOSSIBLE"))

mat = []
start = (None, None)
for i in range(R):
    row = list(input())
    if "X" in row:
        start = (i, row.index("X"))
    mat.append(row)
dir = {0:"D",1:"L",2:"R",3:"U"}
directions = [(1,0), (0,-1),(0,1),(-1,0)]
swap = {"D":"U","L":"R","U":"D","R":"L"}
out = []
y, x = start
for _ in range(k//2):
    for i, (dy, dx) in enumerate(directions):
        newY, newX = y+dy, x+dx

        if min(newY, newX) == -1 or newY == R or newX == C or mat[newY][newX] == "*":
            continue

        y,x = newY, newX
        out.append(dir[i])
        break
    else:
        exit(print("IMPOSSIBLE"))

print("".join(out))
