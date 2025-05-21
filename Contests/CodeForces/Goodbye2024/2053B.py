from collections import defaultdict
from itertools import cycle, groupby
def inc_group(l):
    res = [[l[0]]]
    for i in range(1, len(l)):
        if l[i-1] == l[i] -1:
            res[-1].append(l[i])
        else:
            res.append([l[i]])
    return res

for tc in range(int(input())):
    N = int(input())
    ans = []
    must = defaultdict(int)
    
    qs = []
    for _ in range(N):
        l,r = list(map(int, input().replace(","," ").split()))
        if l == r: must[l] += 1
        qs.append((l,r))
    bad = sorted(list(must.keys()))
    #print(bad)
    if not bad:
        badranges = []
    else:
        badranges = list(inc_group(bad))
    #print(badranges)

    for l, r in qs:
        if l == r:
            if must[l] > 1:
                ans.append(0)
            else: ans.append(1)
        else:
            for rng in badranges:
                if len(rng) == 1:
                    bl = rng[0]
                    br = rng[0]
                else:
                    bl = rng[0]
                    br = rng[-1]
                if bl<= l and br>=r:
                    ans.append(0)
                    break

            else:
                ans.append(1)
    print("".join(map(str, ans)))

