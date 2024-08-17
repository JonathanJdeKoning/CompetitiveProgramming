n,m,a,b = map(int, input().split())
if m >= n:
    exit(print(min(b, n*a)))
one = a*n
from math import ceil
two = ceil((n/m))*b

print(min(one, two))
