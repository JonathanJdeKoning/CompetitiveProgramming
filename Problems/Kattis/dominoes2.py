from collections import defaultdict
for _ in range(int(input())):
    numNodes, numEdges, numQs = map(int, input().split())
    edges = defaultdict(list)

    for _ in range(numEdges):
        u,v = map(int, input().split())
        edges[u].append(v)

    seen = set()
    ans = 0
    for _ in range(numQs):
        q = int(input())

        if q not in seen:
            s = [q]
            while s:
                curr = s.pop()
                if curr in seen: continue
                seen.add(curr)
                ans += 1

                for edge in edges[curr]:
                    if edge in seen: continue
                    s.append(edge)
    print(ans)


