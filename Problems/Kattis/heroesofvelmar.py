power = {
"Shadow": 6,
"Gale": 5,
"Ranger": 4,
"Anvil": 7,
"Vexia": 3,
"Guardian": 8,
"Thunderheart": 6,
"Frostwhisper": 2,
"Voidclaw": 3,
"Ironwood": 3,
"Zenith": 4,
"Seraphina": 1
}
p1 = [[],[],[]]
p2 = [[],[],[]]

for i in range(3):
    p1[i] = input().split()[1:]
    p2[i] = input().split()[1:]
p1Powers = [0,0,0]
p2Powers = [0,0,0]

for i, loc in enumerate(p1):
    if i==1 and "Zenith" in loc: p1Powers[i] += 5
    if "Thunderheart" in loc and len(loc) == 4:
        p1Powers[i] += 6*loc.count("Thunderheart")
    for name in loc:
        if name == "Seraphina":
            p1Powers[i] += 1+(loc.count("Seraphina")-1)
        else:
            p1Powers[i] += power[name] + loc.count("Seraphina")


for i, loc in enumerate(p2):
    if i==1 and "Zenith" in loc: p2Powers[i] += 5
    if "Thunderheart" in loc and len(loc) == 4:
        p2Powers[i] += 6*loc.count("Thunderheart")
    for name in loc:
        if name == "Seraphina":
            p2Powers[i] += 1+(loc.count("Seraphina")-1)
        else:
            p2Powers[i] += power[name] + loc.count("Seraphina")

p1Locs = 0
p2Locs = 0

for i in range(3):
    if p1Powers[i] > p2Powers[i]:
        p1Locs += 1
    if p2Powers[i] > p1Powers[i]:
        p2Locs += 1

if p1Locs > p2Locs:
    print("Player 1")
elif p2Locs > p1Locs:
    print("Player 2")
elif p1Locs == p2Locs:
    if sum(p1Powers) > sum(p2Powers):
        print("Player 1")
    elif sum(p2Powers) > sum(p1Powers):
        print("Player 2")
    elif sum(p1Powers) == sum(p2Powers):
        print("Tie")




