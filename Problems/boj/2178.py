from collections import deque
def solve():
    q = deque([(0,0)])
    R, C = map(int, input().split())
    mat = [list(map(int,list(input()))) for _ in range(R)]
    seen = set(q)
    steps = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        steps += 1

        for _ in range(len(q)):
            curr = q.popleft()
            if curr == (R-1, C-1): return steps 
            for dy, dx in directions:
                y = curr[0] + dy
                x = curr[1] + dx

                if min(y,x) == -1 or y==R or x==C or (y,x) in seen: continue
                if mat[y][x] ==0: continue
                
                q.append((y,x))
                seen.add((y,x))
print(solve())
