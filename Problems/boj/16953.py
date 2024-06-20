a, b = map(int, input().split())
from collections import deque
q = deque([b])

steps = 0
found = False
while q:
    steps += 1
    for _ in range(len(q)):
        curr = q.popleft()
        if curr == a:
            found = True;print(steps);break
        if curr == 1: continue
        if str(curr)[-1] == "1":
            q.append(int(str(curr)[:-1]))
        if curr%2==0:
            q.append(curr//2)
    if found: break
else:
    print(-1)

