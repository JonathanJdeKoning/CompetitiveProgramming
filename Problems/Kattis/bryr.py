import heapq
from collections import defaultdict
edges = defaultdict(list)

numNodes, numEdges = map(int, input().split())
for _ in range(numEdges):
    u,v,w = map(int, input().split())
    edges[u].append((v,w))
    edges[v].append((u,w))
    
h = [(0,1)]
seen = set()

while h:
    currWeight, currNode = heapq.heappop(h)
    if currNode == numNodes: print(currWeight);break
    if currNode in seen: continue
    seen.add(currNode)

    for edgeNode, edgeWeight in edges[currNode]:
        if edgeNode in seen: continue
        newdist = edgeWeight + currWeight
        
        heapq.heappush(h, (newdist, edgeNode))
        
        
