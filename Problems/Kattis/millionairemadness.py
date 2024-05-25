R, C = map(int ,input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
start = (0,0)
end = (R-1, C-1)

import heapq
from collections import defaultdict, deque
seen = set()
directions = [(0,-1),(0,1),(-1,0),(1,0)]


h = [(0,start)]
ans = 0  
while h:
    currWeight,(currY,currX) = heapq.heappop(h)
    currVal = grid[currY][currX]
    ans = max(ans, currWeight)
    if (currY, currX) == end:
        print(ans)
        break
    if (currY, currX) in seen: continue
    seen.add((currY, currX))
    
    for dy, dx in directions:
        newY, newX = currY+dy, currX+dx
        
        if min(newY, newX) < 0 or newY == R or newX == C or (newY, newX) in seen: continue
        
        nextVal = grid[newY][newX]
        reach = 0 if nextVal <= currVal else nextVal-currVal
        
        heapq.heappush(h,(reach, (newY, newX)))

        

