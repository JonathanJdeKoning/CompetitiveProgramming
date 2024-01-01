precincts, _districts = list(map(int, input().split()))
districts = {}
bigtotal = 0
atotal = 0
btotal = 0
for _ in range(precincts):
    data = list(map(int, input().split()))
    assigned = data[0]
    
    if assigned not in districts:
        districts[assigned] = ["",0,0]

    districts[assigned][1]+= data[1]
    districts[assigned][2]+= data[2]

for key, val in districts.items():
    total = val[1] + val[2]; bigtotal += total
    if val[1] > val[2]: 
        val[0] ="A"
        awaste = val[1]-((total//2)+1)
        val[1] = awaste
        atotal+= awaste
        btotal+= val[2]
    else: 
        val[0] = "B"
        bwaste = val[2] - ((total//2)+1)
        val[2] = bwaste
        btotal += bwaste
        atotal += val[1]


ewwww = abs(atotal - btotal)/bigtotal
districts = dict(sorted(districts.items()))
for data in districts.values():
    print(" ".join(str(x) for x in data))

print(ewwww)
