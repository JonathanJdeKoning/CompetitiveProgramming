R, C = map(int, input().split())

a = []
for _ in range(R):
    row = list(input())
    if len(set(row)) != 1: exit(print("NO"))
    a.append(row[0])

from itertools import pairwise

for x,y in pairwise(a):
    if x==y: exit(print("NO"))

print("YES")

