import itertools
mylist = []
for i in range(9):
    mylist.append(int(input()))

possible = list(itertools.combinations(mylist, 7))

for poss in possible:
    if sum(poss) == 100:
        print("\n".join([str(n) for n in poss]))