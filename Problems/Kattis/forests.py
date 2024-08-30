from collections import Counter
d = {}

P, T = map(int, input().split())
for i in range(1,P+1):
    d[i] = [False]*(T+1)

while True:
    try:
        p,t = map(int, input().split())
    except:break
    d[p][t] = True


print(len(Counter(list(map(tuple, d.values())))))
