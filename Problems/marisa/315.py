from math import gcd

a,b = map(int, input().split())


while gcd(a,b) != 1:
    g = gcd(a,b)
    a//=g
    b//=g

print(a,b)
