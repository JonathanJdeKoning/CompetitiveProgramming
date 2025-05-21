mat = []
inst = []
mp = {
    "#": ["#", "#"],
    ".": [".", "."],
    "O": ["[", "]"],
    "@": ["@", "."]
}
with open("day15.in", "r") as file:
    for x in file.readlines():
        if "#" not in x:
            inst.extend(list(x.strip()))
        else:
            row = []
            for c in x[:-1]:
                row.extend(mp[c])
            mat.append(row)

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

def move_side_cells(ny,nx, dy,dx):
    boxes = []
    cy = ny
    cx = nx
    while mat[cy][cx] in "[]":
        boxes.append((cy,cx, mat[cy][cx]))
        cy += dy
        cx += dx
    if mat[cy][cx] == "#":
        return 0
    mat[ny][nx] = "."
    for y,x, char in boxes:
        mat[y+dy][x+dx] = char
    return 1

def move_vert_cells(ny,nx, dy, dx):
    dfs = [(ny,nx)]
    seen = set()
    while dfs:
        cy, cx = dfs.pop()
        if mat[cy][cx] == "#": return 0
        if mat[cy][cx] == ".": continue
        if (cy, cx, mat[cy][cx]) in seen: continue
        seen.add((cy, cx, mat[cy][cx]))
        if mat[cy][cx] == "[":
            dfs.append((cy, cx+1))
            dfs.append((cy+dy, cx ))
        if mat[cy][cx] == "]":
            dfs.append((cy, cx-1))
            dfs.append((cy+dy, cx))

    for y,x, char in list(seen):
        mat[y][x] = "."
    for y, x, char in list(seen):
        mat[y+dy][x+dx] = char
    return 1

for instruction in inst:
    dy,dx = mp[instruction]

    ny, nx = py+dy, px+dx
    if mat[ny][nx] == "#": continue
    if mat[ny][nx] == ".":
        py, px = ny, nx
        continue

    if dy == 0:
        if move_side_cells(ny,nx,dy,dx):
            py, px = ny, nx
    else:
        if move_vert_cells(ny,nx,dy,dx):
            py, px = ny, nx
 
ans = 0
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == "[":
            ans += 100*i+j
print(ans)