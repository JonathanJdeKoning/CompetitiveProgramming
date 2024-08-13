H, W = map(int, input().split())
currY, currX = map(int, input().split())
currY-=1
currX -=1
mat = [list(input()) for _ in range(H)]

inst = input()

for c in inst:
    if c == "U":
        y = currY-1
        x = currX
        if y!= -1 and mat[y][x] == ".":
            currY, currX = y,x
    elif c == "D":
        y = currY+1
        x = currX
        if y!= H and mat[y][x] == ".":
            currY, currX = y,x
    elif c == "L":
        y = currY
        x = currX -1
        if x!= -1 and mat[y][x] == ".":
            currY, currX = y,x
    elif c == "R":
        y = currY
        x = currX+1
        if x!= W and mat[y][x] == ".":
            currY, currX = y,x

print(currY+1, currX+1)



