import heapq
from collections import defaultdict
numNodes, numEdges, start, end = map(int, input().split())
edges = defaultdict(list)

for _ in range(numEdges):
    u,v,w = map(int, input().split())
    edges[u].append((v,w))
    edges[v].append((u,w))

h = [(0, start)]
seen = set()
while h:
    currDist, currNode = heapq.heappop(h)
    if currNode in seen: continue
    seen.add(currNode)

    if currNode == end:
        print(currDist)
        break

    for edgeNode, edgeWeight in edges[currNode]:
        if edgeNode in seen: continue
        heapq.heappush(h, (currDist+edgeWeight, edgeNode))


