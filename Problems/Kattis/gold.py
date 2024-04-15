from collections import deque

total = 0
cols, rows = map(int, input().split())
start = (None, None)
mat = []
for i in range(rows):
    row = list(input())
    if "P" in row:
        start = (i, row.index("P"))
    mat.append(row)

q = deque([start])
seen = set()
directions = [(0,-1),(0,1),(-1,0),(1,0)]
while q:
    curr = q.popleft()
    val = mat[curr[0]][curr[1]]
    if curr in seen: continue
    if val == "G": total += 1
    seen.add(curr)

    next = []
    for dy, dx in directions:
        y = curr[0] + dy
        x = curr[1] + dx
        
        if y==0 or x==0 or y==rows or x == cols or (y,x) in seen or mat[y][x] == "#":
            continue
        next.append((y,x))
    bad = False
    for poss in next:
        if mat[poss[0]][poss[1]] == "T":
            bad = True
            break
    if not bad:
        for poss in next:
            q.append(poss)
print(total)


