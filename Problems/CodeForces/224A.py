a,b,c = map(float, input().split())

from math import sqrt


x = sqrt((a*b)/c)
y = sqrt((b*c)/a)
z = sqrt((a*c)/b)

print(int(4*(x+y+z)))
