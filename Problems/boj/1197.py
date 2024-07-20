import heapq
from collections import defaultdict

numNodes, numEdges = map(int, input().split())
edges = defaultdict(list)
total = 0
for _ in range(numEdges):
    a,b, w = map(int, input().split())
    edges[a].append((b,w))
    edges[b].append((a,w))

h = [(0,1)]
used =set()
while h:
    currDist, currNode = heapq.heappop(h)
    if currNode in used: continue
    used.add(currNode)
    total += currDist
    for edgeNode, edgeDist in edges[currNode]:
        if edgeNode in used: continue
        heapq.heappush(h,(edgeDist, edgeNode))
print(total)

