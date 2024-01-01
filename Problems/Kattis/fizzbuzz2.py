cands, vals = list(map(int, input().split()))
our = []

for i in range(1,vals+1):
    out =""
    if i%3==0: out+="fizz"
    if i%5==0: out+="buzz"
    if out == "": out+=str(i)
    our.append(out)

res = 1
leastbad = 999
for x in range(cands):
    candfizz = input().split()
    bad = 0
    for i,word in enumerate(our):
        if candfizz[i]!= word:
            bad+=1
    if bad < leastbad:
        leastbad = bad
        res = x
print(res+1)
