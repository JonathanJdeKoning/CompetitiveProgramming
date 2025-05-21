from collections import deque
from math import sqrt
from decimal import Decimal
amx = sqrt(5)
bmx = sqrt(3)
cmx = sqrt(2)
tol = 0.0003
q = deque([(0,0,0,-1,-1,-1, "")])
steps = -1
seen = set()
parents = {(0,0,0): (-1,-1,-1, "")}
def get_hist(a,b,c,op):
    out = []
    while True:
        a,b,c,op = parents[(a,b,c)]
        out.append(op)
        if a == -1 and b == -1 and c == -1:
            return out[::-1]


while q:
    steps += 1
    for _ in range(len(q)):
        a,b,c,pa,pb,pc, op = q.popleft()
        if (a,b,c) in seen: continue
        seen.add((a,b,c))
        parents[(a,b,c)] = (pa,pb,pc, op)
        if abs(a-1) <=tol or abs(b-1)<=tol or abs(c-1) <= tol: exit(print(steps, get_hist(a,b,c,op)))

        q.append((amx, b, c,a,b,c, "TA"))
        q.append((a, bmx, c,a,b,c, "TB"))
        q.append((a, b, cmx,a,b,c, "TC"))
        q.append((0,b,c,a,b,c, "AS"))
        q.append((a,0,c,a,b,c, "BS"))
        q.append((a,b,0,a,b,c, "CS"))
        if a != 0:
            btrans = min(a, bmx-b)
            ctrans = min(a, cmx-c)
            q.append((a-btrans, b+btrans, c,a,b,c, "AB"))
            q.append((a-ctrans, b, c+ctrans,a,b,c, "AC"))
        if b != 0:
            atrans = min(b, amx-a)
            ctrans = min(b, cmx-c)
            q.append((a+atrans, b-atrans, c,a,b,c, "BA"))
            q.append((a, b-ctrans, c+ctrans,a,b,c, "BC"))
        if c != 0:
            atrans = min(c, amx-a)
            btrans = min(c, bmx-b)
            q.append((a+atrans, b, c-atrans,a,b,c, "CA"))
            q.append((a, b+btrans, c-btrans,a,b,c, "CB"))

