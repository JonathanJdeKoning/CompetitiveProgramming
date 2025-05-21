from functools import cache
N, P, Q = list(map(int, input().replace(","," ").split()))
s = input()
t = len(s)

def getConsts(x):
    for a in range(101):
        for b in range(101):
            if a*P + b*Q == x:
                return (a,b)
    return (-1,-1)

x,y = getConsts(t)
if x == -1 and y == -1: exit(print(-1))

print(x + y)
idx = 0
for _ in range(x):
    print(s[idx:idx+P])
    idx += P

for _ in range(y):
    print(s[idx: idx+Q])
    idx += Q

            