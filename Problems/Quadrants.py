while True:
    x, y = map(float, input().split())
    if (x,y) == (0,0):
        print("AXIS")
        break
    if 0 in [x,y]:
        print("AXIS")
        continue

    if x>0 and y>0:
        print("Q1")
    elif x < 0 and y<0:
        print("Q3")
    elif x>0 and y<0:
        print("Q4")
    else:
        print("Q2")