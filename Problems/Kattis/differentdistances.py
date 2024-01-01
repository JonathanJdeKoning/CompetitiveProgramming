import math

while True:
    test = list(map(float, input().split()))
    
    if test[0] == 0:break

    x1,y1,x2,y2,p = test[0],test[1],test[2],test[3],test[4]
    
    xmin = math.pow(abs(x1-x2),p)
    ymin = math.pow(abs(y1-y2),p)
    
    print(math.pow((xmin+ymin), (1/p)))