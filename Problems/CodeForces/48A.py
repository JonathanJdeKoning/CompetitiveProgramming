from collections import Counter
F = input()
M = input()
S = input()
fq = Counter([F,M,S])

if len(fq) == 3 or len(fq) == 1: exit(print("?"))
mx = None
mn = None

for k,v in fq.items():
    if v == 2:
        mx = k
    else:
        mn = k


if (mn == "rock" and mx == "scissors") or (mn == "paper" and mx == "rock") or (mn == "scissors" and mx == "paper"):
    if F == mn: print("F")
    elif M == mn: print("M")
    else:
        print("S")
else:
    print('?')