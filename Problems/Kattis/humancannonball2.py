from math import sin, cos
g = 9.81
def fX(t):
    return v*t*cos(th)

def fY(t):
    return v*t*sin(th)-(g*t*t)/2


for _ in range(int(input())):
    v, th, x, h1, h2 = map(float, input().split())
    for i in range(1,2000):
        print(f"{fY(i/100)},{fX(i/100)}")



