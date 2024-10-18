N = int(input())
from itertools import groupby, pairwise

A = list(map(int, input().split()))

g = groupby(A)
best = 0
F = []
for k,v in g:
    F.append(len(list(v)))
for av,bv in pairwise(F):
    best = max(best, 2*min(av, bv))

print(best)    
