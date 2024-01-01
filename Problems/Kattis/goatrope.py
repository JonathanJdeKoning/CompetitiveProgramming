import math
px,py,x1,y1,x2,y2 = list(map(int, input().split()))
xmin,xmax,ymin,ymax = min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2)
rx = (xmin+xmax)/2
ry = (ymin+ymax)/2
rwidth = xmax-xmin
rheight = ymax - ymin

dx = max(abs(px-rx) - rwidth/2,0)
dy = max(abs(py-ry)-rheight/2, 0)
print(math.sqrt(dx*dx+dy*dy))