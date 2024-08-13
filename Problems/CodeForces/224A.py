a,b,c = map(int, input().split())
from math import sqrt
x = sqrt(a*b/c)
y = sqrt(c*b/a)
z = sqrt(a*c/b)

print(f"{a*b/c} {c*b/a} {a*c/b}")

print(x,y,z)
print(int(4*(x+y+z)))







