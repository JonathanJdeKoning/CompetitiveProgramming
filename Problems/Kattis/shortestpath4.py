import heapq
from collections import defaultdict

for _ in range(int(input())):
    input()
    edges = defaultdict(list)
    numNodes = int(input())
    for node in range(numNodes):
        data = list(map(int, input().split()))
        numEdges = data[0]
        for edge in range(1,numEdges*2+1, 2):
            edges[node].append((data[edge], data[edge+1]))


    numQs = int(input())
    for _ in range(numQs):
        seen = set()
        start, end, k = map(int, input().split())

        h = [(0,start,1)]

        while h:
            currDist, currNode, currLen = heapq.heappop(h)
             
            if currNode == end:
                if currLen > k: continue
                else:
                    print(currDist)
                    break

            if currNode in seen or currLen >= k:continue
            if currNode != end:
                seen.add(currNode)

            for edgeNode, edgeDist in edges[currNode]:
                if edgeNode in seen: continue
                heapq.heappush(h, (edgeDist+currDist, edgeNode, currLen+1))
        else:
            print(-1)
    print()



