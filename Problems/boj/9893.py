numNodes, numEdges = map(int, input().split())

from collections import defaultdict, deque
edges = defaultdict(list)

for _ in range(numEdges):
    u,v,w = map(int, input().split())
    edges[u].append((v,w))

q = deque([(0,0)])
poss = []
bigseen = set()
while q:
    bingo = False
    lilseen = set()
    for _ in range(len(q)):
        currDist, currNode = q.popleft()
        if currNode in bigseen: continue
        lilseen.add(currNode)

        if currNode == 1:
            bingo=True
            poss.append(currDist)

        if not bingo:
            for edgeNode, edgeDist in edges[currNode]:
                if edgeNode not in bigseen: q.append((edgeDist+currDist, edgeNode))
    bigseen = bigseen.union(lilseen)
    if bingo: break
print(min(poss))



