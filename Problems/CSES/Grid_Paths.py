R, C =7,7
mat = [[0]*R for _ in range(C)]
N = R*C-1
s = input()
directions = [(-1,0),(0,1),(1,0),(0,-1)]


sy,sx = 0,0
ey, ex = 0,6

q = deque([(sy, sx)])

for c in s:
    for _ in range(len(q)):
        cy, cx = q.popleft()
        for dy, dx in directions:
            ny, nx = cy+dy, cx+dx
            if min(ny, nx) == -1 or ny==R or nx==C: continue

