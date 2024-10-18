N = int(input())
s = input()
mat = []
for i in range(0,N):
    mat.append(list(s[i*N:i*N+N]))

directions = [(1,2),(2,1),(-1,2),(1,-2),(2,-1),(-2,1),(-2,-1),(-1,-2)]
find = "ICPCASIASG"
stack = []
curr = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] == find[curr]:
            stack.append((i,j,curr + 1))


while stack:
    currY, currX, seek = stack.pop()
    if seek == len(find): exit(print("YES"))
    for dy,dx in directions:
        y, x = currY+dy, currX+dx
        if min(y,x) < 0 or max(y,x) >=N or mat[y][x] != find[seek]:
            continue
        stack.append((y,x,seek+1))

print("NO")
