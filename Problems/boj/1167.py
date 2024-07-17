n = int(input())
from collections import defaultdict

edges = defaultdict(list)
for _ in range(n):
    data = list(map(int, input().split()))
    edges[data[0]] = data[1:-1]
print(edges)
