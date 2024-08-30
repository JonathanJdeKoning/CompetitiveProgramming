from collections import defaultdict
edges = defaultdict(list)
numTrans, numQs = map(int, input().split())

for _ in range(numTrans):
    start, end = input().split()
    edges[start].append(end)

reachable = defaultdict(set)
for c in "abcdefghijklmnopqrstuvwxyz":
    s = [c]
    seen = set()
    while s:
        curr = s.pop()
        if curr in seen: continue
        reachable[c].add(curr)
        seen.add(curr)

        for edge in edges[curr]:
            if edge not in seen:
                s.append(edge)


for _ in range(numQs):
    a, b = input().split()
    if len(a) != len(b): print("no"); continue
    for x,y in zip(a,b):
        if not y in reachable[x]:
            print("no")
            break
    else:
        print("yes")
