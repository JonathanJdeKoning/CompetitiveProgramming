from collections import defaultdict
numNodes, numEdges = map(int, input().split())
edges = defaultdict(list)
owed = [int(input()) for _ in range(numNodes)]

for _ in range(numEdges):
    u,v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

seen = set()

for x in range(numNodes):
    if x not in seen:
        balance = 0

        s = [x]
        while s:
            curr = s.pop()
            if curr in seen: continue
            seen.add(curr)
            balance += owed[curr]

            for edge in edges[curr]:
                if edge in seen: continue
                s.append(edge)
        if balance != 0:
            exit(print("IMPOSSIBLE"))
print("POSSIBLE")



