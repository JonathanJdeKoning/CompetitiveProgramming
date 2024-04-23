from collections import defaultdict
from collections import deque
for _ in range(int(input())):
    numnodes = int(input())
    numedges = int(input())
    edges = defaultdict(list)
    for _ in range(numedges):
        u,v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        
    components = 0
    toexplore = list(range(numnodes))
    seen = set()
    for exp in toexplore:
        if exp in seen:continue
        components += 1
        q = deque([exp])
        while q:
            curr = q.popleft()
            if curr in seen: continue
            seen.add(curr)
            
            for edge in edges[curr]:
                q.append(edge)
    print(components -1)
    
