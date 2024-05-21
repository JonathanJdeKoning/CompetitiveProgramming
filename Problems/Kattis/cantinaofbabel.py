from collections import defaultdict
edges = defaultdict(list)
people = set()
for _ in range(int(input())):
    data = input().split()
    name = data[0]
    people.add(name)
    fluent = data[1]
    understands = data[2:]

    edges[name].append(fluent)
    edges[fluent].append(name)
    for lang in understands:
        edges[lang].append(name)

seen = set()
s = []
def dfs(node):
    if node in seen: return
    seen.add(node)
    for edge in edges[node]:
        dfs(edge)
    s.append(node)
for edge in edges:
    dfs(edge)

new = defaultdict(list)

for name, langs in edges.items():
    for lang in langs:
        new[lang].append(name)
#print(s)

seen = set()
sizes = []

for node in s[::-1]:
    stack = [node]
    size = 0
    while stack:
        curr = stack.pop()
        if curr in seen: continue
        seen.add(curr)
        if curr in people: size += 1

        for edge in new[curr]:
            stack.append(edge)
    sizes.append(size)
print(len(people)-max(sizes))

