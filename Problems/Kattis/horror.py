from collections import defaultdict, deque
N, H, L = list(map(int, input().replace(","," ").split()))
horrors = list(map(int, input().replace(","," ").split()))
edges = defaultdict(list)
for _ in range(L):
    u, v = list(map(int, input().replace(","," ").split()))
    edges[u].append(v)
    edges[v].append(u)

ids = {i:99999999 for i in range(N)}
seen = set()
q = deque(horrors)
hi = -1
while q:
    hi += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr in seen: continue
        seen.add(curr)
        ids[curr] = hi

        for edge in edges[curr]:
            if edge in seen: continue
            q.append(edge)
mx = max(list(ids.values()))
print(min([k for k,v in ids.items() if v == mx]))

