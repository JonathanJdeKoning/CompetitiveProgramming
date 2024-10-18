from itertools import groupby
record = [len(input())-7 for _ in range(int(input()))]
y = None
n = None
g = groupby(record)
mx = 0
mxs = []
for k,v in g:
    v = list(v)
    if len(v) > mx:
        mxs = [k]
        mx = len(v)
    elif len(v) == mx:
        mxs.append(k)

if len(set(mxs))!=1:
    y=-1
else:
    y=mxs[0]
mxLead = 0
bestLead = 0
leads = []
yC = 0
nC = 0

for x in record:
    if x == 0:yC += 1
    else: nC += 1

    diff = yC-nC
    if abs(diff) > mxLead:
        if diff > 0:
            bestLead = 0
        else:
            bestLead = 1
        mxLead = abs(diff)
        leads = [bestLead]
    elif abs(diff) == mxLead:
        if diff > 0:
            leads.append(0)
        else:
            leads.append(1)
if len(set(leads)) != 1:
    n = -1
else:
    n = bestLead

if y==n:
    print("Agree")
else:
    print("Disagree")

#print(f"{y=} {n=}")
