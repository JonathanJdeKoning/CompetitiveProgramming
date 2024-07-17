n,m = map(int, input().split())
s, e = map(int, input().split())
from collections import defaultdict, deque
seen = set()
edges = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

q = deque([s])
steps = -1
while q:
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr == e:
            print(steps)
            break
        if curr in seen: continue
        seen.add(curr)

        for edge in edges[curr]:
            if edge not in seen:
                q.append(edge)
        q.append(curr+1)
        q.append(curr-1)
    else:...
    break
