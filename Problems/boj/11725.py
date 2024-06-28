nodeCount = int(input())
from collections import defaultdict, deque
edges = defaultdict(list)

for _ in range(nodeCount-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

q = deque([1])
seen = set()
ans = defaultdict(int)

while q:
    curr = q.popleft()
    if curr in seen:continue
    seen.add(curr)

    for child in edges[curr]:
        q.append(child)
        if child not in seen:
            ans[child] = curr

for i in range(2, nodeCount+1):
    print(ans[i])


