from collections import defaultdict
from graphlib import TopologicalSorter
edges = {}
N, K = list(map(int, input().replace(","," ").split()))
for i in range(N): edges[i] = []
for _ in range(N):
    u, v = list(map(int, input().replace(","," ").split()))
    edges[u-1].append(v-1)


def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
 
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]

print(find_SCC(edges))