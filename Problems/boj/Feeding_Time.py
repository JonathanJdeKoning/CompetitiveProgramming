directions = [(y,x) for y in (-1,0,1) for x in (-1,0,1) if (y,x) != (0,0)]
C, R = list(map(int, input().split()))
mat = [list(input()) for _ in range(R)]
mx = 0
seen = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if mat[i][j] == "*" or seen[i][j]: continue
        field = 0
        q = [(i,j)]
        while q:
            currY, currX = q.pop()
            if seen[currY][currX]: continue
            seen[currY][currX] = 1 
            field += 1

            for dy, dx in directions:
                newY, newX = currY+dy, currX +dx

                if min(newY, newX) == -1 or newY == R or newX == C or seen[newY][newX] or mat[newY][newX] == "*": continue
                q.append((newY, newX))
        mx = max(mx, field)
print(mx)
