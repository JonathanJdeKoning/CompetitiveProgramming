def solve():
    R, C = map(int, input().split())
    mat = []
    start = None
    for i in range(R):
        row = list(input())
        if "S" in row:
            start = (i, row.index("S"))
        mat.append(row)
    from collections import deque
    q = deque([start])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    steps = -1
    seen = set()
    good = {"0", "O","G"}
    while q:
        steps += 1
        for _ in range(len(q)):
            currY, currX = q.popleft()
            if mat[currY][currX] == "G": return(f"Shortest Path: {steps}")
            if (currY, currX) in seen: continue
            seen.add((currY, currX))

            for dy, dx in directions:
                y = dy + currY
                x = dx + currX

                if min(y, x) == -1 or y==R or x==C or mat[y][x] not in good or (y,x) in seen: continue
                q.append((y,x))
    return "No Exit"

for _ in range(int(input())):
    print(solve())


