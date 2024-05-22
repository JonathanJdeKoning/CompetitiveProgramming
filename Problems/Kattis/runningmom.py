from collections import defaultdict
edges = defaultdict(list)
for _ in range(int(input())):
    s, e = input().split()
    edges[s].append(e)
    x = edges[e]

order = []
seen = set()
def dfs(node):
    if node in seen: return
    seen.add(node)
    for edge in edges[node]:
        dfs(edge)
    order.append(node)
for edge in edges:
    if edge not in seen:
        dfs(edge)

new = defaultdict(list)
for node, to in edges.items():
    for edge in to:
        new[edge].append(node)

seen = set()
bad = set()
for node in order[::-1]:
    stack = [node]
    size = 0
    while stack:
        curr = stack.pop()
        if curr in seen: continue
        seen.add(curr)
        size += 1

        for edge in new[curr]:
            stack.append(edge)
    if size == 1:
        bad.add(node)

while True:
    try:
        q = input()
        if q in bad:
            print(f"{q} trapped")
        else:
            print(f"{q} safe")
    except:
        break
