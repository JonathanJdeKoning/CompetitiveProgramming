from collections import deque, defaultdict
N = int(input)
edges = defaultdict(list)
for _ in range(N-1):
    u,v = list(map(int, input().replace(","," ").split()))
    edges[u].append(v)
    edges[v].append(u)
