import heapq
from collections import defaultdict

numNodes, numEdges = map(int, input().split())
edges = defaultdict(list)

for _ in range(numEdges):
    u,v,w = map(int, input().split())
    edges[u].append((v,w))
    edges[v].append((u,w))
parents = [-1]*(numNodes+1)
seen = set()
h = [(0,1,-1)]

while h:
    currWeight, currNode, parent = heapq.heappop(h)
    if currNode in seen: continue
    seen.add(currNode)

    parents[currNode] = parent
    for edgeNode, edgeWeight in edges[currNode]:
        if edgeNode in seen: continue
        newdist = edgeWeight+currWeight
        heapq.heappush(h, (newdist, edgeNode, currNode))

out = [numNodes]
begin = numNodes
while True:
    new = parents[begin]
    if new == -1: break
    out.append(new)
    begin = new
if len(out) == 1:
    print(-1)
else:
    print(" ".join([str(x) for x in out[::-1]]))
