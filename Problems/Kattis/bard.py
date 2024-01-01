from collections import defaultdict
_villagers = int(input())
_nights = int(input())
villagers = defaultdict(list)
allofem = []
for night in range(_nights):
    data = list(map(int, input().split()))
    
    _people = data[0]
    present = data[1:]

    if 1 in present:
        for person in present:
            villagers[person].append(night)
        allofem.append(night)
    else:
        known = []
        for person, songs in villagers.items():
            known.extend(songs)
        known = list(set(known))
        for person in present:
            villagers[person] = known.copy()


good = []
for villy, songs in villagers.items():
    if sorted(songs) == sorted(allofem):
        good.append(villy)

print("\n".join([str(x) for x in sorted(good)]))
