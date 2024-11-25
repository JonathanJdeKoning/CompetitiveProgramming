from collections import Counter
A = []
B = []
suitMap = {"2": 2, "3": 3, "4":4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T":10, "J": 11, "Q":12, "K": 13, "A": 14}
ans = -1
def points(hand):
    vals = [x[0] for x in hand]
    suits = [x[1] for x in hand]
    
    mxVal = max(vals)
    mxFreq = max(Counter(vals).values())
    flush = len(set(suits)) == 1
    straight = sorted(vals) == list(range(min(vals), max(vals)+1))

    if flush and straight and mxVal == 14: return (10, 9999)
    elif flush and straight: return (9, mxVal)
    elif mxFreq == 4: return (8, sorted(vals)[2])
    elif len(set(vals)) == 2: return (7, sorted(vals)[2])
    elif flush: return (6, mxVal)
    elif straight: return (5, mxVal)
    elif mxFreq == 3: return (4, sorted(vals)[2])
    elif len(set(vals)) == 3: return (3, sorted(vals)[3])
    elif mxFreq == 2: return (2, [k for k,v in Counter(vals).items() if v==2][0])
    else: return (1, mxVal)


with open("poker.txt", "r") as file:
    for line in file.readlines():
        line = line.strip().split()
        A.append([(suitMap[x[0]], x[1]) for x in line[:5]])
        B.append([(suitMap[x[0]], x[1]) for x in line[5:]])

for aHand, bHand in zip(A,B):
    oldAns = ans
    aType, aTie = points(aHand)
    bType, bTie = points(bHand)
    if aType > bType:
        ans += 1
    elif aType==bType:
        aVals = sorted([x[0] for x in aHand])
        bVals = sorted([x[0] for x in bHand])

        if aTie > bTie:
            ans += 1
        elif aTie==bTie:
            for a,b in zip(aVals, bVals):
                if a!=b:
                    if a > b:
                        ans += 1
                    break

    print(aHand, bHand)
    print(aType, bType)
    print(aTie, bTie)
    if oldAns == ans: print(2, ans)
    else: print(1, ans)

print(ans)

