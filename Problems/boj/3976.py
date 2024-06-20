import heapq
from collections import defaultdict
for _ in range(int(input())):
    data = list(map(int, input().split()))
    numPoints = data[0]
    longA,longB,shootA,shootB = data[1:]
    fromAtoB = list(map(int, input().split()))
    dribblesA = list(map(int, input().split()))
    fromBtoA = list(map(int, input().split()))
    dribblesB = list(map(int, input().split()))
    
    edges = defaultdict(list)

    edges["D"] = [("A0", longA),("B0", longB)]
    edges["A"+str(numPoints-1)].append(("G", shootA))
    edges["B"+str(numPoints-1)].append(("G", shootB))
    for i in range(0,numPoints-1):
        edges["A" + str(i)].append(("A"+str(i+1), dribblesA[i]))
        edges["A" + str(i)].append(("B"+str(i+1), fromAtoB[i]))
        edges["B" + str(i)].append(("B"+str(i+1), dribblesB[i]))
        edges["B" + str(i)].append(("A"+str(i+1), fromBtoA[i]))
    
    h = [(0,"D")]
    seen = set()
    while h:
        currDist, currNode = heapq.heappop(h)
        if currNode in seen: continue
        seen.add(currNode)
        if currNode == "G": print(currDist);break
        for edgeNode, edgeDist in edges[currNode]:
            heapq.heappush(h, (currDist+edgeDist, edgeNode))







