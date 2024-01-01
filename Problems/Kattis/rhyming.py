word = input()
numlines = int(input())

endings = []

for _ in range(numlines):
    endings.append(input().split())

goodendings = []

for ending in endings:
    good = False
    for end in ending:
        if word.endswith(end):
            good = True
            break
    if good:
        for end in ending:
            goodendings.append(end)
    else:
        continue
    

tryme = int(input())
for line in range(tryme):
    test = input()
    
    good = False
    for word in goodendings:
        if test.endswith(word):
            good = True
            break
    if good:
        print("YES")
    else:
        print("NO")

