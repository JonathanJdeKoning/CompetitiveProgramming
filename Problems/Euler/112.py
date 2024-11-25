
from decimal import Decimal
non = Decimal(0)
bounce = Decimal(0)
n = []
b = []
for i in range(1,1000000000):
    l = list(str(i))
    if l == sorted(l) or l == sorted(l, reverse=True):
        non += 1
    else:
        bounce += 1
    try:
        ratio = 100*(bounce/i)
    except: continue
    if i%1000 == 0: print(i, ratio)
    if i == 538:
        print(i, ratio)
    if i == 21780:
        print(i, ratio)
    if ratio == 99:
        print(i, ratio)
        break