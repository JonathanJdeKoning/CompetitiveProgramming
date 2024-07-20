import heapq
n, k = map(int, input().split())
from collections import defaultdict
mat = []
h = []
used = set()
edges = defaultdict(list)
seen = set()
for i in range(n):
    row = list(map(int, input().split()))
    for j, cell in enumerate(row):
        used.add(cell)
        if cell == 1:
            h.append((0, (i,j)))
        else:
            edges[cell-1].append((i,j))
    mat.append(row)
if len(used) != k:print(-1);exit(0)
while h:
    currDist, (currY, currX) = heapq.heappop(h)
    if (currY, currX) in seen: continue
    seen.add((currY, currX))
    if mat[currY][currX] == k: print(currDist); exit(0)

    for edgeY, edgeX in edges[mat[currY][currX]]:
        if (edgeY, edgeX) in seen: continue
        newDist = currDist + abs(currY - edgeY) + abs(currX - edgeX)
        heapq.heappush(h, (newDist, (edgeY, edgeX)))
