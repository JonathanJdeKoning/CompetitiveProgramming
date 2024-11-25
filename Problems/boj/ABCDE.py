N, K = list(map(int, input().split()))
from collections import defaultdict
edges = defaultdict(list)
for _ in range(K):
    u, v = list(map(int, input().split()))
    edges[u].append(v)
    edges[v].append(u)


def dfs(node, length, seen):
    if length == 5: exit(print(1))
    for edge in edges[node]:
        if edge not in seen:
            seen.add(edge)
            dfs(edge, length + 1, seen)
            seen.discard(edge)



for node in range(N):
    dfs(node, 1, set([node]))

print(0)