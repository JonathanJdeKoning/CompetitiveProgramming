from collections import Counter
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = Counter()
for x in a:
    for y in b:
        v = y/x
        if v.is_integer():
            c[int(v)] += 1

print(c[max(c.keys())])
