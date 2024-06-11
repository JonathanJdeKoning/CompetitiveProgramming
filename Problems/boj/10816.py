input()
from collections import Counter
c = Counter(input().split())
input()
out = []
for x in input().split():
    out.append(str(c[x]))
print(" ".join(out))
