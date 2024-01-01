lines = int(input())
concs = []
good = True
for i in range(lines):
    line = input().split()

    if line[0] == "->":
        concs.append(line[-1])
    else:
        pivot = line.index("->")
        asss = line[:pivot]
        conq = line[-1]
        for ass in asss:
            if ass not in concs:
                print(i+1)
                good = False
                break
        concs.append(conq)

if good:
    print("correct")
