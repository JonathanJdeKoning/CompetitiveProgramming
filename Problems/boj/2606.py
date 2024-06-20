from collections import defaultdict, deque

compCount = int(input())
edgeCount = int(input())

edges = defaultdict(list)
for _ in range(edgeCount):
    s,e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

q = deque([1])
count = -1
seen = set(q)

while q:
    curr = q.popleft()
    count += 1

    for child in edges[curr]:
        if child not in seen:
            q.append(child)
            seen.add(child)

print(count)
