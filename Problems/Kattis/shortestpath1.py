import heapq
from math import inf
from collections import defaultdict

while True:
    edges = defaultdict(list)
    
    numNodes, numEdges, numQueries, startIdx = map(int, input().split())
    if [numNodes, numEdges, numQueries, startIdx] == [0,0,0,0]: break
    
    for _ in range(numEdges):
        u,v,w = map(int, input().split())
        edges[u].append((v,w))
        #edges[v].append((u,w))
    
    dists = [-1]*numNodes
    
    h = [(0, startIdx)]
    seen = set()
    
    while h:
        currWeight, currNode = heapq.heappop(h)
        if currNode in seen: continue
        seen.add(currNode)
        dists[currNode] = currWeight
        
        for edgeNode, edgeWeight in edges[currNode]:
            if edgeNode in seen: continue
            newdist = currWeight+edgeWeight
            heapq.heappush(h, (newdist, edgeNode))
    
    for _ in range(numQueries):
        dist = dists[int(input())]
        if dist == -1: print("Impossible")
        else: print(dist)


    print()
