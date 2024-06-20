import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

ds = list(map(int, input().split()))
rs = list(map(int, input().split()))

targs = list(zip(rs, ds))

base = targs[0][0]
mult = targs[0][1]

for nextR, nextMod in targs[1:]:
    while base%nextMod != nextR:
        base += mult
    mult = lcm(mult, nextMod)
print(base)
