left = {"U":"L", "L":"D", "D":"R", "R":"U"}
right = {"U":"R", "L":"U", "D":"L", "R":"D"}
def move(y,x,dir,op):
    if op == "F":
        if dir == "U":
            return (y+1, x, dir)
        elif dir == "L":
            return (y, x-1, dir) 
        elif dir == "R":
            return (y, x+1, dir)
        elif dir == "D":
            return (y-1, x, dir)
    elif op == "B":
        if dir == "U":
            return (y-1, x, dir)
        elif dir == "L":
            return (y, x+1, dir) 
        elif dir == "R":
            return (y, x-1, dir)
        elif dir == "D":
            return (y+1, x, dir)
    elif op == "L":
        return (y,x, left[dir])
    elif op == "R":
        return (y,x,right[dir])


for _ in range(int(input())):
    s = input()
    mxY, mxX = 0,0
    mnY, mnX = 0,0
    dir = "U"
    y, x = 0,0
    for c in s:
        y, x, dir = move(y,x, dir, c)
        mxY, mnY = max(mxY, y), min(mnY, y)
        mxX, mnX = max(mxX, x), min(mnX, x)
    #print(f"{mnY=}, {mxY=}")
    #print(f"{mnX=}, {mxX=}")
    print(abs(mnY-mxY)*abs(mnX-mxX))

