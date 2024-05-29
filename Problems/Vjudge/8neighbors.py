mat = []
n,m = map(int, input().split())
mat.append(["x"]*(m+2))
for _ in range(n):
    mat.append(["x"]+list(input())+["x"])
i,j = map(int, input().split())


mat.append(["x"]*(m+2))
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for dy, dx in directions:
    y = i+dy
    x = j+dx
    if mat[y][x] != "x":
        print("no")
        break
else:
    print("yes")
