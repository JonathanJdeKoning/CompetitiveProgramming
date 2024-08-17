n = int(input())
mat = [list(input()) for _ in range(n)]
directions = [(0,1),(1,0),(-1,0),(0,-1)]
for i in range(n):
    for j in range(n):
        a = 0
        for dy, dx in directions:
            y = dy+i
            x = dx+j

            if min(y,x) == -1 or max(y,x) == n: continue
            if mat[y][x] == "o": a += 1
        if a%2==1: exit(print("NO"))
print("YES")


