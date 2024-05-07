numPlanets, numTunnels = map(int, input().split())
start, end = map(int, input().split())
from collections import defaultdict,deque
d = defaultdict(list)

for _ in range(numTunnels):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
def solve():
    q = deque([start])
    n = -1
    seen = set()
    while q:
        n += 1
        for _ in range(len(q)):
            curr = q.popleft()
            if curr in seen: continue
            if curr == end: return n
            seen.add(curr)

            for node in d[curr]:
                q.append(node)
from math import ceil
print(ceil(solve()/2))


