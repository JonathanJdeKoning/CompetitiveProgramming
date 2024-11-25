from fractions import Fraction
badboys = []
for num in range(11, 100):
    for den in range(num+1, 100):
        nn = list(str(num))
        dd = list(str(den))

        for i,c in enumerate(nn):
            if c == "0": continue
            if c in dd:
                x = dd.index(c)

                newN = nn[:i] + nn[i+1:]
                newD = dd[:x] + dd[x+1:]
                try:
                    if int(newN[0]) / int(newD[0]) == num/den:
                        badboys.append((num, den))
                except: continue

base = Fraction(badboys[0][0], badboys[0][1])
for num, den in badboys[1:]:
    base*= Fraction(num,den)

print(base)


