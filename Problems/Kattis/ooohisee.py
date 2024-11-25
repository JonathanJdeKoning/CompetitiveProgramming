R, C = list(map(int, input().split()))
mat = [list(input()) for _ in range(R)]
directions = [(x,y) for x in [-1,0,1] for y in [-1,0,1] if (x,y) != (0,0)]

loc = []
for i in range(1,R-1):
    for j in range(1,C-1):
        if mat[i][j] == "0":
            for dy, dx in directions:
                if mat[i+dy][j+dx] != "O":
                    break
            else:
                loc.append((i+1, j+1))

if not loc:
    print("Oh no!")
elif len(loc) != 1:
    print(f"Oh no! {len(loc)} locations")
else:
    print(*loc[0])
