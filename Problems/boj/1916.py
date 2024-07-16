import heapq
from collections import defaultdict
edges = defaultdict(list)

seen = set()

numNodes = int(input())
numEdges = int(input())

for _ in range(numEdges):
    s, e, w = map(int, input().split())
    edges[s].append((e,w))

start, end = map(int, input().split())

h = [(0,start)]

while h:
    currWeight, currNode = heapq.heappop(h)
    if currNode in seen: continue
    if currNode == end: print(currWeight);break
    seen.add(currNode)

    for edgeNode, edgeWeight in edges[currNode]:
        if edgeNode in seen: continue
        heapq.heappush(h, (edgeWeight+currWeight, edgeNode))
