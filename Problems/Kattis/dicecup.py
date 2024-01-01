from collections import defaultdict
n,m = list(map(int, input().split()))

outs = defaultdict(int)

for i in range(1,n+1):
    for j in range(1,m+1):
        outs[i+j]+=1

res = []

max = 0
for key, val in outs.items():
    if val > max:
        max = val

for key, val in outs.items():
    if val == max:
        res.append(key)

print("\n".join([str(x) for x in sorted(res)]))
