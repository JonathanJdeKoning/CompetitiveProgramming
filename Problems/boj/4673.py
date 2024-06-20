bad = set()
for i in range(1,10001):
    bad.add(i+sum([int(x) for x in str(i)]))

for i in range(1,10001):
    if i not in bad:
        print(i)
