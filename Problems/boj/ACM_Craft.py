# Created by Jonathan de Koning on 2025-01-02 [>_]

from graphlib import TopologicalSorter
from collections import defaultdict 
for tc in range(int(input())):
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    
    edges = defaultdict(list)
    for _ in range(K):
        start, end = map(int, input().split())
        edges[end].append(start)
    
    dp = [0]*(N+1)
    for k in range(1, N+1):
        if k not in edges: dp[k] = C[k-1]
    
    ts = list(TopologicalSorter(edges).static_order())
    for node in ts:
        dp[node] = C[node-1] + max([dp[p] for p in edges[node]], default=0)
    W = int(input())
    print(dp[W])