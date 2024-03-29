
for i in range(int(input())):
    intro, extro, univ = map(int , input().split())
    tents = intro

    tents += extro//3
    leftover = extro%3

    if leftover == 0:
        tents += univ//3
        tents += 1 if univ%3!=0 else 0
    else:
        need = (3-leftover)
        if univ < need:
            print(-1)
        else:
            tents += 1
            univ -= need
            tents += univ//3
            tents += 1 if univ%3!=0 else 0
    print(tents)


