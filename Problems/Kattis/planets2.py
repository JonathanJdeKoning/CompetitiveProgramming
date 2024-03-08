first = int(input())
wack = {}
for i in range(first):
    data = input().split()
    name = data[0]
    wack[name] = data[2:]

yo = int(input())
yoyo = {}
for i in range(yo):
    data = input().split()
    yoyo[data[1]] = int(data[0]) 

fin = {}
for k, v in wack.items():
    total = 0
    for vv in v:
        try:
            total += yoyo[vv]
        except:continue
    fin[k] = total
tups = []
for k, v in fin.items():
    tups.append((k,v))
tups = sorted(tups)
for tup in tups:
    print(tup[0], tup[1])
    
