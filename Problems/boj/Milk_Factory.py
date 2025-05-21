from collections import defaultdict
N = int(input())
edges = defaultdict(list)

for _ in range(N-1):
    u, v = list(map(int, input().replace(","," ").split()))
    edges[u].append(v)
allem = set(range(1, N+1))
for i in range(1, N+1):
    stack = [i]
    seen = set()
    while stack:
        curr = stack.pop()
        if curr in seen: continue
        seen.add(curr)
        for edge in edges[curr]:
            if edge not in seen:
                stack.append(edge)
            
    allem = allem.intersection(seen)
if not allem: print(-1)
else:
    print(min(allem))