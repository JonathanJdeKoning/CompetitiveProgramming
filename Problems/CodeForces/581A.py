a,b = map(int, input().split())
one = min(a,b)
a -= one
b -= one
try:
    last = [x for x in [a,b] if x][0]
except:
    last = 0
from math import ceil, floor
two = floor(last/2)
print(one,two)
