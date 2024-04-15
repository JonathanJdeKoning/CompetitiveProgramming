from collections import deque

total = 0
cols, rows = map(int, input().split())

mat = []
for i in range(rows):
    row = list(input())
    if "P" in row:
        start = (i, row.index("P"))
    mat.append(row)

q = deque([start])
seen = set()
ds = [(0,-1),(0,1),(-1,0),(1,0)]
while q:
    c = q.popleft()
    val = mat[c[0]][c[1]]
    if c in seen: continue
    if val == "G": total += 1
    seen.add(c)

    next = [(c[0]+y,c[1]+x) for y,x in ds if mat[c[0]+y][c[1]+x]!="#"] 
    if not "T" in [mat[x[0]][x[1]] for x in next]: q.extend(next)
print(total)


