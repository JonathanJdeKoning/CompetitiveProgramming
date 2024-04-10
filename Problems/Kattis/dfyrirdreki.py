a = int(input())
b = int(input())
c = int(input())
from math import sqrt
if (b*b >= (4*a*c) and a != 0):
    root = sqrt(b*b - (4*a*c))
    plus = (-1*b + root) / (2*a)
    minus = (-1*b - root) / (2*a)
    if plus == minus:
        print(1)
    else:
        print(2)
else:
    print(0)
