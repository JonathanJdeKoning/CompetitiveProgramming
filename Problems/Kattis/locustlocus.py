import math
lines = int(input())

yearlist = []

def lcm(a,b):
    return abs(a*b) // math.gcd(a,b)

for line in range(lines):
    year, x, y = list(map(int, input().split()))
    mylcm = lcm(x,y)

    yearlist.append(mylcm+year)
print(min(yearlist))