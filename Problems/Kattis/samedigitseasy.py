s,e = list(map(int, input().split()))
from collections import Counter
pairs = []
for i in range(s,e+1):
    for j in range(i, e+1):
        p = i*j
        if p <= 99999: continue
        if p > 999999: continue
        if Counter(str(i)+str(j)) == Counter(str(p)):
            pairs.append((i,j,p))
print(f"{len(pairs)} digit-preserving pair(s)")
for pair in pairs:
    print(f"x = {pair[0]}, y = {pair[1]}, xy = {pair[2]}")
