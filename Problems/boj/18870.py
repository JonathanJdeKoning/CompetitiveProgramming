from collections import defaultdict, Counter
n = int(input())

a = list(map(int, input().split()))
fq = Counter(a)
d = defaultdict(int)
pref = 0

for k, v in sorted(fq.items()):
    d[k] = pref
    pref += 1

out = []
for num in a:
    out.append(d[num])

print(" ".join(map(str, out)))



