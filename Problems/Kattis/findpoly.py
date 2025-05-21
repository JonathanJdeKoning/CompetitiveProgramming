from collections import defaultdict
edges = defaultdict(list)
while True:
    try:
        s = input()
    except EOFError: break
    for segment in s.split(";"):
        if not segment: continue
        segment = segment.strip()
        points = segment.split("),(")
        points[0] = points[0][1:]
        points[1] = points[1][:-1]
        points = [tuple(list(map(int, p.split(",")))) for p in points]
        edges[points[0]].append(points[1])
        edges[points[1]].append(points[0])

figs = 0
polies = 0
seen = set()
for point in edges:
    if point in seen: continue
    figs += 1
    poly = True
    dfs = [point]
    
    while dfs:
        curr = dfs.pop()
        if curr in seen: continue
        seen.add(curr)
        connections = edges[curr]
        if len(connections) != 2: poly = False

        for conn in connections:
            if conn not in seen:
                dfs.append(conn)
    if poly: polies += 1
print(figs, polies)