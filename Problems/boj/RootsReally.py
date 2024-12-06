from math import sqrt, inf
for _ in range(int(input())):
    a,b,c,s,t = list(map(int, input().split()))
    try:
        v = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        w = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    except ValueError:
        print("No")
        continue

    if (v >= s and v <=t) or (w >= s and w<=t):
        print("Yes")
    else:
        print("No")

