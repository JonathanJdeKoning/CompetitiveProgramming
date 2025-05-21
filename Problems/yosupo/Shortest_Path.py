import heapq
from collections import defaultdict
N, M, S, T = list(map(int, input().replace(","," ").split()))
edges = {i: [] for i in range(N)}

for _ in range(M):
    u,v, w = list(map(int, input().replace(","," ").split()))
    edges[u].append((w, v))


h = [(0, S, -1)]
seen = set()
parents = defaultdict(int)
parents[S] = -1
while h:
    cW, cN, cP= heapq.heappop(h)
    if cN in seen: continue
    seen.add(cN)
    parents[cN] = cP
    if cN == T: break
    for eW, eN in edges[cN]:
        if eN not in seen:
            heapq.heappush(h, (eW+cW, eN, cN))
else:
    exit(print(-1))

best = cW
numEdges = -1
trav = []
while cN != -1:
    numEdges += 1
    trav.append((cN, cP))
    cP = cN
    cN = parents[cN]
print(trav)
print(best, numEdges)
for u,v in trav[::-1][:-1]:
    print(u,v)


