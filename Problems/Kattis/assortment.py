from sys import stdin

s = stdin.readline()
for _ in range(int(stdin.readline())):
    start, end = list(map(int, stdin.readline().split()))
    slice = s[start-1:end]
    
    order = "ATGC"
    alls = [(x, slice.count(x)) for x in "ACTG"]

    while len(alls) > 0:
        tryme, to = alls[:], []
        mx = max([x[1] for x in alls])
        for x in tryme:
            if x[1] == mx:
                to.append(x[0])
                alls.remove(x)
        to = sorted(to, key=lambda x:order.index(x))
        print("".join(to), end="")
    print()
