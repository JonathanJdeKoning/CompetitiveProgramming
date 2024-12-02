N = int(input())
mat = []
babyY = None
babyX = None
for i in range(N):
    row = list(map(int, input().split()))
    if 9 in row:
        babyY, babyX = (i, row.index(9))
        row[row.index(9)] = 0
    mat.append(row)

ans = 0
size = 2
until = 2
directions = [(0,1),(1,0),(-1,0),(0,-1)]
done = False
log = []
from collections import deque
while True:
    time = 0
    found = False
    q = deque([(babyY, babyX)])
    seen = set()
    while q:
        time += 1
        fishies = []
        for _ in range(len(q)):
            currY, currX = q.popleft()
            if (currY, currX) in seen: continue
            seen.add((currY, currX))


            for dy, dx in directions:
                newY, newX = currY+dy, currX+dx
                if min(newY, newX) == -1 or newY == N or newX == N or (newY, newX) in seen or mat[newY][newX] > size: continue
                if mat[newY][newX] != 0 and mat[newY][newX] < size:
                    fishies.append((newY, newX))
                q.append((newY, newX))

        if fishies:
            fishies.sort()
            closestY, closestX = fishies[0]
            until -= 1
            if until == 0:
                size += 1
                until = size
            log.append((time,ans+time, (closestY, closestX)))
            mat[closestY][closestX] = 0
            babyY, babyX = closestY, closestX
            found = True
            ans += time
            break

        if found: break
    else: break

        

print(ans)
#for row in log: print(row)