from words import *
from collections import defaultdict
mp = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    mp[key].append(word)

sq = defaultdict(list)
sqs = defaultdict(set)
for i in range(31625):
    x = i**2
    sq[len(str(x))].append(x)
    sqs[len(str(x))].add(x)


mx = 0
new = {}
for k,v in mp.items():
    if len(v) > 1:
        new[k] = v
for w in new.values():
    base = w[0]
    other = w[1]
    l = len(base)
    uniq = len(set(list(base)))

    for i in sq[l]:
        ltd = {}
        dtl = {}
        good = True
        used = set()
        for c,d in zip(base, str(i)):
            if d in dtl and dtl[d] != c:
                good = False
                break
            ltd[c] = d
            dtl[d] = c
        if not good: continue

        v = int("".join(list(map(lambda c: ltd[c], other))))
        if v in sqs[l]:
            if max(v,i) > mx:
                mx = max(v,i)

print(mx)

