from math import floor, ceil 
from collections import defaultdict
import heapq

def solve():
    edges = defaultdict(list)

    currAttack, startHealth = map(int, input().split())
    numAreas, numPassages = map(int, input().split())

    for _ in range(numPassages):
        start, end, enemyAttack, enemyHealth = map(int, input().split())
        edges[start].append((end, enemyAttack, enemyHealth))

    h = [(-startHealth,1)]
    seen = set()
    while h:
        currHealth, currNode = heapq.heappop(h)
        if currNode in seen: continue
        seen.add(currNode)
        if currNode == numAreas: return -currHealth

        for edgeNode, enemyAttack, enemyHealth in edges[currNode]:
            loss = enemyAttack * (ceil(enemyHealth/currAttack)-1)
            if currHealth+loss >= 0: continue

            heapq.heappush(h, (currHealth+loss, edgeNode))
    
    return "Oh no"

print(solve())


