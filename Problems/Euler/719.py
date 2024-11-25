curr = 0
mx = 10^4
ans = 0
from itertools import combinations, chain
x = [1, 2, 3, 4,5,6]
subsets = [v for a in range(len(x)) for v in combinations(x, a)]
for i in range(len(subsets)//2 + 1):
    print(list(chain(subsets[i])), ' ', [e for e in x if e not in subsets[i]])
"""
while True:
    curr += 1
    x = curr*curr
    if x <10: continue
    if x > mx: break
    for sub in allsubs(str(x)):
        if sum()
"""