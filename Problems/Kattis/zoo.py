listnum = 1
while (True):
    animals = int(input())

    if animals == 0: break

    animallist = []
    animaldict = {}
    for i in range(animals):
        animallist.append(input().split()[-1].lower())
    for animal in sorted(animallist):
        animaldict[animal] = animallist.count(animal)
    
    print(f"List {listnum}:")

    for animal, count in animaldict.items():
        print(f"{animal} | {count}")
    
    listnum += 1