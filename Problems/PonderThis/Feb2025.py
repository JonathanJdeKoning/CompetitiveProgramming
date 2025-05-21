from primes import *
total = len(allOdd)
print(f"{total}\n")
print(allOdd)
progress = 0
for dig in "1379":
    poss = dig4[dig].intersection(allOdd)
    for h4 in poss:
        progress += 1
        if progress % 10 == 0: print(f"{100*(progress/total)}%")
        for v4 in poss:
            if h4[-1] != v4[-1]: continue
            for d1 in dig0[v4[0]].intersection(dig4[h4[0]]):
                for d0 in dig2[d1[2]].intersection(dig4[h4[-1]]):
                    for h1 in dig1[d0[1]].intersection(dig3[d1[1]]).intersection(dig4[v4[1]]):
                        pass
                        #print(h1)
print("Done")