s = list(input())
from collections import Counter
fq = Counter(s)
mx = s[0]

for k,v in fq.items():
    mx = max(mx, k*v)
    
print(mx)
