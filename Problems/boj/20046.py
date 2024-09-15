import heapq
from collections import defaultdict

R,C = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]
directions = [(0,1),(1,0),(-1,0),(0,-1)]
start = (0,0)
end = (R-1, C-1)

if mat[0][0] ==-1 or mat[R-1][C-1] == -1:exit(print(-1))

h = [(mat[0][0],start)]
seen = set()
while h:
    currDist, (y,x) = heapq.heappop(h)
    if (y,x) in seen: continue
    seen.add((y,x))

    if (y,x) == end:
        print(currDist)
        break

    for dy,dx in directions:
        newY, newX = dy+y, dx+x

        if min(newY, newX) == -1 or newY==R or newX ==C or (newY, newX) in seen or mat[newY][newX] ==-1:
            continue
        heapq.heappush(h,(currDist+mat[newY][newX], (newY, newX)))
else:
    print(-1)



