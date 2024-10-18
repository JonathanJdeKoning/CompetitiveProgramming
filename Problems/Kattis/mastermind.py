from collections import defaultdict
N, S, T = input().split()
N = int(N)
r,s = 0,0
ds = defaultdict(int)
dt = defaultdict(int)
for a,b in zip(S,T):
    if a==b:
        r += 1
    else:
        ds[a] += 1
        dt[b] += 1


for k, v in dt.items():
    s += min(v,ds[k])

print(r,s)
