s = input()
from collections import defaultdict

d = defaultdict(int)

for i in range(0,10):
    n = input()
    d[n] = i

out = []
for i in range(0,len(s)-1,10):
    chk = s[i:i+10]

    out.append(str(d[chk]))

print("".join(out))



