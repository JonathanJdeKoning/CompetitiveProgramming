from graphlib import TopologicalSorter
from collections import defaultdict

ans = [0,0]
edges = defaultdict(list)
lines = [line.strip() for line in open("day5.in", "r").readlines()]
for line in lines:
    if not line: continue
    
    if "|" in line:
        before, after = line.split("|")
        edges[before].append(after)
        continue
 
    old = line.split(",")
    mid = len(old) // 2

    ts = TopologicalSorter({k:v for k, v in edges.items() if k in old})
    good = list(ts.static_order())[::-1]

    mp = {n:i for i, n in enumerate(good)} 
    new = sorted(old, key=lambda n: mp[n])

    ans[int(new!=old)] += int(new[mid])

print(*ans, sep="\n")