n = int(input())
input()
from math import inf
mn = inf

for _ in range(n):
    line = list(map(int, input().split()))
    mn = min(mn,15*len(line)+ 5*sum(line))

print(mn)
