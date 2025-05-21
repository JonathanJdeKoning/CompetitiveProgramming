from collections import defaultdict
from functools import cache
designs = []
towels = []
lines = [line.strip() for line in open("day19.in", "r")]
designs = lines[0].split(", ")
towels = lines[2:]
ans = 0
pref = defaultdict(list)
for design in designs:
    pref[design[0]].append(design)

@cache
def ways_to_make(s):
    if not s: return 1
    start = s[0]
    poss = 0
    for p in pref[start]:
        if s.startswith(p):
            poss += ways_to_make(s[len(p):])
    return poss


for towel in towels:
    ans += ways_to_make(towel)
print(ans)