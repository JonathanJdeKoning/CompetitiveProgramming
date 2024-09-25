from collections import deque 
color = {}
graph = [[1,3],[0,2],[1,3],[0,2]]
currCol = 0
for i in range(len(graph)):
    if i not in color:
        q = deque([i])

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr in color and color[curr] != currCol: exit(print(False)) 
                color[curr] = currCol

                for edge in graph[curr]:
                    if edge in color and color[edge] == currCol: exit(print(False)) 
                    if edge not in color: q.appendleft(edge)
            currCol = abs(currCol - 1)
print(True)