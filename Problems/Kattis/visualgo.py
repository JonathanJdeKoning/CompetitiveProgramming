import heapq
from collections import defaultdict
numNodes, numEdges = map(int, input().split())

edges = defaultdict(list)

for _ in range(numEdges):
    u,v,w = map(int, input().split())
    edges[u].append((v, w))

start, end = map(int, input().split())

h = [(0, start)]
good = set()
found = False
best = -99999
ans = 0
while h:
    print(h)
    currWeight, currNode = heapq.heappop(h)
    if found and currWeight > best:
        continue
    if currNode == end:
        if not found:
            found = True
            best = currWeight
            ans += 1
        else:
            if currWeight == best:
                ans+= 1

    for edgeNode, edgeWeight in edges[currNode]:
        if found and edgeWeight+currWeight > best:
            continue
        heapq.heappush(h, (edgeWeight+currWeight, edgeNode))

print(ans)
