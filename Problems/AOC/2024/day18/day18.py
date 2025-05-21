N = 71
mat = [["."]* N for _ in range(N)]
barr = []
with open("day18.in", "r") as file:
    for line in file.readlines():
        x,y = map(int, line.strip().split(","))
        barr.append((y,x))



for by, bx in barr[:1024]:
    mat[by][bx] = "#"

from collections import deque

directions = [(-1,0),(0,1),(1,0),(0,-1)]
def shortest():
    q = deque([(0,0)])
    steps = -1
    seen = set()
    while q:
        steps += 1
        for _ in range(len(q)):
            currY, currX = q.popleft()
            if (currY, currX) in seen: continue
            if (currY, currX) == (N-1, N-1):
                return steps
            seen.add((currY, currX))


            for dy, dx in directions:
                y,x = currY + dy, currX+dx 

                if min(y,x) == -1 or y ==N or x==N or (y,x) in seen or mat[y][x] == "#": continue
                q.append((y,x))
    return -1
for i, (by,bx) in enumerate(barr[1024:], start=1025):
    mat[by][bx] = "#"
    steps = shortest()
    if i == 1025: print(steps)
    if steps == -1:
        exit(print(f"{bx},{by}"))
