from collections import defaultdict
from collections import deque
nodeCount, edgeCount, start = map(int, input().split())

edges = defaultdict(list)

for _ in range(edgeCount):
    s, e =map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)
for k in edges.keys():
    edges[k] = sorted(edges[k])

seen = set()
stack = [start]
order = []
while stack:
    curr = stack.pop()
    if curr in seen: continue
    seen.add(curr)
    order.append(curr)

    for child in edges[curr][::-1]:
        stack.append(child)
print(" ".join(map(str, order)))
seen = set()
q = deque([start])
order =[]
while q:
    curr = q.popleft()
    if curr in seen: continue
    seen.add(curr)
    order.append(curr)

    for child in edges[curr]:
        q.append(child)
print(" ".join(map(str, order)))


