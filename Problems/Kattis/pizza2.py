import math
PI = math.pi
r, c= list(map(int, input().split()))

fullarea = PI*r*r
r-=c
cheesearea = PI*r*r

try:
    print((100/(fullarea/cheesearea)))
except ZeroDivisionError: print("0")