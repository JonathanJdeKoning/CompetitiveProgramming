N = int(input())
A = []
for _ in range(N):
    A.append(input().split()[1:])
from itertools import product
combs = [" ".join(x) for x in list(product(*A))]

for c in sorted(combs):
    print(c)


