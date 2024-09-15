a,b,c,d = map(int, input().split())
from math import sqrt
dist = sqrt((a-c)**2 + (b-d)**2)

print(format(round(dist, 2), ".2f"))
