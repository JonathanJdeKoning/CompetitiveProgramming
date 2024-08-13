"""
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets
"""

n,q = map(int, input().split())
#dsu = DisjointSetUnion(n)
from collections import defaultdict
import heapq
edges = defaultdict(list)
for i in range(1,q+1):
    l,r,w = map(int, input().split())

    for j in range(l,r+1):
        edges[n+i].append((j,w))
        edges[j].append((n+i,w))
total = 0
h = [(0,1)]
seen =set()
while h:
    currWeight, currNode = heapq.heappop(h)
    if currNode in seen: continue
    seen.add(currNode)
    total += currWeight

    for edgeNode, edgeWeight in edges[currNode]:
        if edgeNode not in seen:
            heapq.heappush(h, (edgeWeight,edgeNode))
if seen != set(range(1,n+q+1)):
    print(-1)
else:
    print(total)







