import heapq
from collections import defaultdict
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
    
def get_edges(n):
    return mat[n-1]
    
seen = set()
correct = []

h = [(0,1,None)]
found = False
while h and not found:
    currWeight, currNode, parent = heapq.heappop(h)
    if currNode in seen: continue
    seen.add(currNode)
    correct.append((currNode, parent))
    for edgeNode, edgeWeight in enumerate(get_edges(currNode),start=1):
        if edgeNode in seen: continue
        heapq.heappush(h, (edgeWeight, edgeNode, currNode))
        if len(seen) == n:
            found = True
            break
for u,v in correct:
    if not u or not v: continue
    print(u,v)
        
        


