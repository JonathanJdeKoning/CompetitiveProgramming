t = int(input())
from collections import defaultdict

d = defaultdict(int)
for _ in range(t):
    d[input()] += 1

if len(d.keys()) == 1:
    print(d.keys()[0])
else:
    print("blandad best")
