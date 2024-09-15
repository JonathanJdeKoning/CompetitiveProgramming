n = int(input())
cur = 0
from collections import defaultdict
d = defaultdict(list)
cur = 0
swap = True
for num in range(0,n**2):
    cur+=1
    if num%n==0:
        cur -= 1
    cur%=n
    d[cur].append(num+1)
    
for k,v in d.items():
    print(" ".join(map(str, v)))

