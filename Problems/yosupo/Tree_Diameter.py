from collections import defaultdict
import heapq
N = int(input())
seen = set()
edges = defaultdict(list)
for _ in range(N-1):
    u,v,w = list(map(int, input().split()))
    edges[u].append((w,v))
    edges[v].append((w,u))

stack = [u]
end = None
while stack:
    curr = stack.pop()
    if curr in seen: continue
    seen.add(curr)
    isEnd = True
    for edgeW, edgeN in edges[curr]:
        if edgeN not in seen:
            stack.append(edgeN)
            isEnd = False
    if isEnd:
        end = curr
        break

print(end)




