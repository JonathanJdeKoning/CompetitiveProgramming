tests = int(input())
tbs = 0
lrs = 0
for test in range(tests):
    string = input()
    
    if string[0] == "0":
        tbs += 1
    if string[1] == "0":
        tbs += 1
    if string[2] == "0":
        lrs += 1
    if string[3] == "0":
        lrs += 1
    
minslats = min([tbs, lrs])

if minslats%2 == 1:
    minslats = minslats-1

swords = minslats/2

tbs = tbs - swords*2
lrs = lrs - swords*2
    
print(f"{int(swords)} {int(tbs)} {int(lrs)}")
    