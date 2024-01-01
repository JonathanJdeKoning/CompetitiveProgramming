numstops = int(input())

stops = sorted(list(map(int, input().split())))

tog = []

curr = stops[0]
currtog = list([curr])

for stop in stops[1:]:
    if stop == curr + 1:
        currtog.append(stop)
    else:
        tog.append(currtog)
        currtog = [stop]
    curr = stop
tog.append(currtog)

out = ""

for yummers in tog:
    if len(yummers) > 2:
        out+=str(yummers[0])+"-"+str(yummers[-1])
        out += " "
    else:
        for x in yummers:
            outy = str(x)
            out += outy
            out += " "
print(out[:-1])
