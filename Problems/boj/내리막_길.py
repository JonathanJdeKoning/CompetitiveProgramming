R, C = list(map(int, input().replace(","," ").split()))
directions = [(-1,0),(0,1),(1,0),(0,-1)]

ans =0

stack = [(0,0)]
mat = [list(map(int, input().split())) for _ in range(R)]

while stack:
    cy, cx = stack.pop()
    if (cy, cx) == (R-1, C-1): ans += 1
    for dy, dx in directions:
        ny, nx = dy+cy, dx+cx
        if min(ny,nx) == -1: continue
        if ny == R or nx == C: continue
        if mat[ny][nx] >= mat[cy][cx]: continue
        stack.append((ny,nx))
print(ans)