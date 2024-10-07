from collections import deque
R,C = list(map(int, input().split()))

mat = [list(input()) for _ in range(R)]

goats = 0
wolves = 0
seen = set()
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if (i,j) in seen: continue
        
        if cell in "kv":
            q = deque([(i,j)])
            g = 0
            w = 0
            while q:
                curr = q.popleft()

                if curr in seen: continue
                seen.add(curr)
                
                currY, currX = curr
                if mat[currY][currX] == "k": g += 1
                if mat[currY][currX] == "v": w += 1
                for dy,dx in [(-1,0),(0,-1),(1,0),(0,1)]:
                    newY = dy+currY
                    newX = dx+currX

                    if min(newY, newX)==-1 or newY == R or newX == C or (newY, newX) in seen or mat[newY][newX] == "#": continue
                    q.append((newY, newX))
            if g > w:
                goats += g
            else:
                wolves += w
print(goats, wolves)
