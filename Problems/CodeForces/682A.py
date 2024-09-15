n,m = map(int, input().split())
from collections import defaultdict

d = defaultdict(int)

for i in range(n%10+1):
    d[i]+= 1

n-= n%10
x = n//10
for i in range(10):
    d[i]+= x
d[0]-= 1

e = defaultdict(int)

for i in range(m%10+1):
    e[i]+= 1

m-= m%10
x = m//10
for i in range(10):
    e[i]+= x
e[0]-= 1
fives = []

for i in range(0,10):
    for j in range(0,10):
        if (i+j)%5==0: fives.append((i,j))
ans = 0
for a, b in fives:
    ans += d[a]*e[b]

print(ans)

