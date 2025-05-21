from copy import copy
from math import inf
N,M = list(map(int, input().replace(","," ").split()))
stalls = [0]*101
for _ in range(N):
    s,t,c = list(map(int, input().replace(","," ").split()))
    for i in range(s, t+1):
        stalls[i] = c
ans = inf

ac = []
for _ in range(M):
    s,t,p, c = list(map(int, input().replace(","," ").split()))
    ac.append((s,t,p,c))
for mask in range(1<<M):
    ss = copy(stalls)
    price = 0
    for i in range(M):
        if mask & (1<<i):
            s,t,p,c = ac[i]
            for j in range(s, t+1):
                ss[j] -= p
            price += c
    #print(ss)
    #print(price)
    if len([x for x in ss if x > 0]) == 0:
        ans = min(ans, price)
    

print(ans)