from collections import deque
from math import inf
for _ in range(int(input())):
    length, n = map(int, input().split())
    length*=100
    l = []
    r = []

    for _ in range(n):
        carlen, side = input().split()
        carlen = int(carlen)
        if side == "left":
            l.append(carlen)
        else:
            r.append(carlen)
    l.append(inf)
    r.append(inf)
    l.reverse()
    r.reverse()

    curr = "left"
    total = 0
    while len(l)!=1 or len(r)!=1:
        load = length
        if curr == "left":
            while load - l[-1]>0:
                load -= l.pop()
            curr = "right"
            total += 1
        else:
            while load - r[-1]>0:
                load -= r.pop()
            curr = "left"
            total += 1
    print(total)


        

