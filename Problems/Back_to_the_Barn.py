R, C, K = list(map(int, input().replace(","," ").split()))
mat = [list(input()) for _ in range( R )]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
ans = 0


def dfs(cy, cx, l):
    global ans
    if (cy, cx) == (0, C-1):
        if l == K:
            ans += 1
            return
    for dy, dx in directions:
        ny, nx = cy+dy, cx+dx

        if min(ny, nx) == -1 or ny == R or nx == C or mat[ny][nx] == "T": continue

        mat[cy][cx] = "T"
        dfs(ny, nx, l+1)

        mat[cy][cx] = "."
dfs(R-1, 0, 1)
print(ans)