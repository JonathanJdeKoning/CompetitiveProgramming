n = int(input())
a = list(map(int, input().split()))

prev = 0

d = []
from itertools import pairwise
for a,b in pairwise(a):
    d.append((b-a)//abs(b-a))
    
print(d)
