s,e = map(int, input().split())

from collections import deque

if e < s:
    print(s-e)
    exit(0)

q = deque([(s,0)])
seen = set()
while q:
    for _ in range(len(q)):
        currPos, currTime = q.popleft()
        #print(currPos, currTime)
        if currPos == e: print(currTime); break
        if currPos in seen or currPos < 0 or (currPos > e and ((currPos-e) > e-s)): continue
        seen.add(currPos)

        q.appendleft((currPos*2, currTime+1))
        q.append((currPos+1, currTime+1))
        q.append((currPos-1, currTime+1))
    else:
        continue
    break
