from collections import defaultdict, deque
N, M = list(map(int, input().replace(","," ").split()))
edges = defaultdict(list)
for _ in range(M):
    u,v = list(map(int, input().replace(","," ").split()))
    edges[u].append(v)
    edges[v].append(u)

q = deque([0])
seen  =set()
while q:
    c = q.popleft()
    if c in seen: exit(print("no way"))
    seen.add(c)
    for x in edges[c]:
        if x not in seen:
            q.append(x)
print("attend here")



    