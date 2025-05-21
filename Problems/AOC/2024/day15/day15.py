mat = []
inst = []
with open("day15.in", "r") as file:
    for x in file.readlines():
        if "#" not in x:
            inst.extend(list(x)[:-1])
        else:
            mat.append(list(x)[:-1])

class Box:
    def __init__(self, y, x):
        self.y = y
        self.x = x

py, px = None, None
for i, row in enumerate(mat):
    if "@" in row:
        py, px = i, row.index("@")
mat[py][px] = "."

mp = {
    "<": (0,-1),
    ">": (0,1),
    "v": (1, 0),
    "^": (-1, 0)
}       

for instruction in inst:
    dy,dx = mp[instruction]

    ny, nx = py+dy, px+dx
    if mat[ny][nx] == "#": continue
    if mat[ny][nx] == ".":
        py, px = ny, nx
        continue
    
    while mat[ny][nx] == "O":
        ny += dy
        nx += dx
    if mat[ny][nx] == "#": continue
    mat[ny][nx] = "O"
    py,px = py+dy, px+dx
    mat[py][px] = "."
mat[py][px] = "@"
ans = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "O":
            ans += 100 * i+j

print(ans)
