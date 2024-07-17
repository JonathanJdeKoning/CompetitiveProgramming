from collections import defaultdict, deque
def solve():
    numNodes, numLines = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(numLines):
        a,b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    color = {}
    val = 0
    for i in range(1,numNodes+1):
        if i in color:continue
        q = deque([i])
        while q:
            val = abs(val-1)
            for _ in range(len(q)):
                curr = q.popleft()
                if curr in color:
                    if color[curr] != val: return "impossible"
                    else: continue
                else:
                    color[curr] = val

                for edge in edges[curr]:
                    q.append(edge)
    return "possible"


for _ in range(int(input())):
    print(solve())
