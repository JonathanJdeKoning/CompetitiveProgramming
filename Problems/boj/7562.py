from collections import deque
for _ in range(int(input())):
    n = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    q = deque([start])
    directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    steps = -1
    seen = set()
    while q:
        steps += 1
        for _ in range(len(q)):
            currY, currX = q.popleft()
            if (currY, currX) == end:
                print(steps)
                break
            if (currY, currX) in seen: continue
            seen.add((currY, currX))

            for dy, dx in directions:
                y = dy+currY
                x = currX+dx

                if min(y,x) ==-1 or y==n or x==n or (y,x) in seen: continue
                q.append((y, x))
        else: continue
        break
