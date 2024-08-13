n = int(input())
s = input()

from collections import Counter
freq = Counter(s)
if len([v for v in freq.values() if v%n!=0]) >0: exit(print(-1))
ans = []

for k,v in freq.items():
    ans.extend([k]*(v//n))

print(n*"".join(ans))
