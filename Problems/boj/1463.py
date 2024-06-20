n = int(input())
from collections import deque
q = deque([n])

steps = -1
while q:
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr == 1:
            print(steps)
            q = []
            break

        if curr%3==0:
            q.append(curr//3)
        if curr%2==0: 
            q.append(curr//2)
        q.append(curr-1)

