nodeCount, edgeCount = map(int, input().split())

start = int(input())
from math import inf
dist = [inf]*(nodeCount+1)
dist[start] = 0

import heapq 

h =  [(0,start)]
from collections import defaultdict
edges = defaultdict(list)

for _ in range(edgeCount):
    s,e, w = map(int, input().split())
    edges[s].append((e, w))

seen = set()
while h:
    currWeight, currNode = heapq.heappop(h)
    if currNode in seen: continue
    seen.add(currNode)

    for edgeNode, edgeWeight in edges[currNode]:
        if edgeNode in seen: continue
        newdist = currWeight+edgeWeight
        if newdist < dist[edgeNode]:
            dist[edgeNode] = newdist
        heapq.heappush(h,(dist[edgeNode], edgeNode))

for x in dist[1:]:
    if x == inf:
        print("INF")
    else:
        print(x)
