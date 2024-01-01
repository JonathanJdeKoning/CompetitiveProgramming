from collections import defaultdict
data = ""
with open("input.txt", "r") as file:
    data = file.readlines()

seedlist = [int(x) for x in data[0].split(":")[1].split()]
print(f"{seedlist=}")
new = []
for i in range(0,len(seedlist),2):

    seednum = seedlist[i]
    more = seedlist[i+1]
    print(f"{seednum=}")
    print(f"{more=}")

    for j in range(seednum,seednum+more):
        new.append(j)
seeds = {}
for seed in new:
    seed = int(seed)
    seeds[seed] = seed

maps = defaultdict(list)

count = 0
for line in data:
    if not line[0].isdigit():
        if line == "\n":
            count += 1
        continue
    maps[count].append([int(x) for x in line.split()])    
for map, ranges in maps.items():
    for seed, val in seeds.items():
        for myrange in ranges:
            if val >= myrange[1] and val < myrange[1]+myrange[2]:
                diff = myrange[0] - myrange[1]
                seeds[seed] = val + diff

print(min(list(seeds.values())))
