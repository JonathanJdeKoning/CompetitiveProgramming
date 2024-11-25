e = set([89])
o = set([1])
for i in range(2, 10000000):
    if i%100000 == 0: print(i)
    if i in o: continue
    if i in e:
        continue

    loop = [i]
    while True:
        i = sum([int(x)**2 for x in str(i)])

        if i in o:
            for l in loop: o.add(l)
            break
        elif i in e:
            for l in loop: e.add((l))
            break
print(len(e))
