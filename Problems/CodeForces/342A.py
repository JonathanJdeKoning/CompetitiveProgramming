n = int(input())
a = list(map(int, input().split()))

from collections import Counter
k = n//3

fq = Counter(a)

out = []
if 5 in fq or 7 in fq: exit(print(-1))
if fq[1] != k: exit(print(-1))
if fq[3] > fq[6]: exit(print(-1))

for i in range(fq[3]):
    out.append("1 3 6")
fq[6] -= fq[3]
fq[3] = 0

if fq[2] != fq[4]+fq[6]:
    exit(print("-1"))

for _ in range(fq[4]):
    out.append("1 2 4")
for _ in range(fq[6]):
    out.append("1 2 6")
for x in out: print(x)
