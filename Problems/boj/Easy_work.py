N = int(input())
from collections import defaultdict
d =  defaultdict(str)
for _ in range(N):
    name, op = input().split()
    d[name] = op

ins = [x for x in d if d[x] == "enter"]
print("\n".join(sorted(ins, reverse=True)))