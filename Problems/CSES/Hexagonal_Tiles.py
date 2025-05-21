while N:=int(input()):
    x,y=0,1
    for _ in range(N):
        x,y=y,x+y
    print(y)