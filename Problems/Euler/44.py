def p(n):
    return (n*(3*n-1))//2

mx = 10000
curr = 1
pents = [p(n) for n in range(1, mx+1)]
pset = set(pents)
print(pents[:10])
while True:
    if curr%10==0: print(curr)
    for i in range(0,mx-curr):
        a,b = pents[i], pents[i+curr]

        if a+b in pset and b-a in pset:
            exit(print(b-a))
    curr += 1
