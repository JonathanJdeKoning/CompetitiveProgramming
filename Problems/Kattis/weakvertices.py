from collections import defaultdict

while True:
    x = int(input())
    if x == -1: break

    max = [[int(x) for x in input().split()] for _ in range(x)]

    mydict = defaultdict(list)
    weak = []
    for idx, row in enumerate(max):
        if row.count(0) == len(row): weak.append(idx)
        for jdx, col in enumerate(row):
            if col == 1:
                mydict[idx].append(jdx)
    


    for key, vals in mydict.items():
        good = False
        for val in vals:
            for node in mydict[val]:
                if key in mydict[node]:
                    good = True
        if not good:
            weak.append(key)
    print(" ".join(str(x) for x in sorted(weak)))

