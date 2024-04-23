from collections import Counter
n = int(input())
kat = []
dom = []
poss = set()
for _ in range(n):
    verdict = input()
    kat.append(verdict)
    poss.add(verdict)
for _ in range(n):
    verdict = input()
    dom.append(verdict)
    poss.add(verdict)

katD = dict(Counter(kat))
domD = dict(Counter(dom))
total = 0

for p in poss:
    total += min(katD.get(p,0), domD.get(p,0))
print(total)
