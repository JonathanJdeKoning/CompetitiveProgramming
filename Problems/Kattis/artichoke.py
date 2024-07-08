from math import sin, cos

p, a, b, c, d, n = map(int, input().split())

def price(k):
    return p*(sin(a*k+b)+cos(c*k+d)+2)

ans = 0
mx = 0
for i in range(1, n+1):
    new = price(i)
    mx = max(mx, new)
    ans = max(ans, mx-new)

print(ans)
