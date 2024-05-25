from collections import defaultdict
import heapq
while True:
    nodeCount, edgeCount = map(int, input().split())
    if nodeCount+edgeCount == 0: break
    
    edges = defaultdict(list)

    for _ in range(edgeCount):
        start, end, factor = input().split()
        start, end, factor = int(start), int(end), float(factor)

        edges[start].append((end, factor))
        edges[end].append((start, factor))

    h = [(-1,0)]
    seen = set()
    while h:
        currSize, currNode = heapq.heappop(h)
        if currNode == nodeCount-1: print(f"{-currSize:.4f}");break
        if currNode in seen: continue
        seen.add(currNode)

        for edgeNode, edgeFactor in edges[currNode]:
            if edgeNode in seen: continue

            newSize = currSize*edgeFactor
            heapq.heappush(h, (newSize, edgeNode))



