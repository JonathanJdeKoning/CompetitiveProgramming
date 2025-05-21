from collections import defaultdict, deque
N = int(input())
edges = defaultdict(list)

if N == 1:
    exit(print(0))
for _ in range(N-1):
    u,v = list(map(int, input().replace(","," ").split()))
    edges[u].append(v)
    edges[v].append(u)
seen = set()
q = deque([v])
ans = 0
while q:
    for _ in range(len(q)):
        curr = q.popleft()
        if curr in seen: continue
        seen.add(curr)

        for edge in edges[curr]:
            if edge not in seen:
                q.append(edge)
seen = set()
q = deque([curr])
steps = -1
while q:
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr in seen: continue
        seen.add(curr)

        for edge in edges[curr]:
            if edge not in seen:
                q.append(edge)

print(steps) 