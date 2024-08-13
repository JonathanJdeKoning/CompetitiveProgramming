from collections import defaultdict
for _ in range(int(input())):
    n,qs = map(int, input().split())
    a = input()
    b = input()

    apref = [[0]*n for _ in range(27)]
    bpref = [[0]*n for _ in range(27)]

    for i in range(n):
        aC = ord(a[i])-96
        bC = ord(b[i])-96

        for j in range(1,27):
            apref[j][i] = apref[j][i-1]
            bpref[j][i] = bpref[j][i-1]
            if j == aC:
                apref[j][i] += 1
            if j == bC:
                bpref[j][i] += 1
    for x in apref:
        print(x)
    print("############")
    for x in bpref:
        print(x)
    for q in range(qs):
        l,r = map(int, input().split())
        tot = 0

        for i in range(1,27):
            tot += bpref[i][r-1] - apref[i][l-1]
        print(tot//2)

