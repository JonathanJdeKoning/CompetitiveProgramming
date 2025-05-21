qs = []
for _ in range(int(input())):
    target = int(input())
    qs.append(target)

sqs = sorted([(q,i) for i, q in enumerate(qs)])
ans = []
curr = 0

roundHigh = 3
roundMult = 1
while True:
    target, i = sqs[curr]
    if target <= roundHigh:
        roundSize = 3*roundMult
        chunkSize = roundMult
        roundLow = roundHigh - roundSize
        #print(f"{roundLow=}, {roundHigh=}, {chunkSize=}, {roundSize=}")
        if target <= roundLow + chunkSize:
            ans.append((i,f"{roundMult} dolphin{'s'*int(chunkSize!=1)}"))
        elif target <= roundLow + chunkSize*2:
            ans.append((i,f"{roundMult} jump{'s'*int(chunkSize != 1)}"))
        else:
            ans.append((i,"splash"))
        curr += 1
        if curr == len(sqs):
            break
    else:
        roundMult += 1
        roundHigh += 3*roundMult
ans.sort()
print("\n".join([x[1] for x in ans]))
    