numNodes, numEdges = map(int, input().split())
edges = {}
for node in range(1,numNodes+1):
    edges[node] = []
for _ in range(numEdges):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)


from collections import deque


q = deque([(1,None)])
seen = set()
steps = 0
parents = {1: None}
while q:
    steps += 1
    for _ in range(len(q)):
        node, parent = q.popleft()
        if node in seen: continue
        seen.add(node)
        parents[node] = parent
        if node == numNodes:
            print(steps)
            out = []
            while node:
                out.append(node)
                node = parents[node]
            print(" ".join([str(x) for x in out][::-1]))
            q = deque([])
            break


        for child in edges[node]:
            q.append((child, node))
