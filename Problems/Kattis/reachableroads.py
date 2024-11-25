from collections import defaultdict
for _ in range(int(input())):
    numNodes = int(input())
    numEdges = int(input())

    edges = defaultdict(list)
    for _ in range(numEdges):
        u,v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        
    components = 0
    seen = set()
    for node in range(numNodes):
        if node in seen:continue
        
        components += 1
        stack = [node]
       
        while stack:
            curr = stack.pop()
            if curr in seen: continue
            
            seen.add(curr)
            
            for edge in edges[curr]:
                stack.append(edge)
    
    print(components - 1)
    
