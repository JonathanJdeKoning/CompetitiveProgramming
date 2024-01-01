while True:
    w,l = list(map(int, input().split()))
    if w == 0 and l == 0: break
    x,y,tx,ty = 0,0,0,0
    steps = int(input())

    for step in range(steps):
        data = input().split()
        op = data[0]
        feet = int(data[1])
        
        if op == "u":
            ty+=feet
            y+= feet
            if y > l-1:
                y=l-1

        elif op == "d":
            ty -=feet
            y-=feet
            if y<0:
                y=0
        elif op == "r":
            tx+=feet
            x += feet
            if x > w-1:
                x=w-1

        elif op == "l":
            tx -=feet
            x-=feet
            if x < 0:
                x = 0
    print(f"Robot thinks {tx} {ty}")
    print(f"Actually at {x} {y}")

