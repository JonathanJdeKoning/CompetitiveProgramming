p = set()
h = set()

for i in range(1000000):
    p.add((i*(3*i-1))//2)
    h.add(i*(2*i-1))

for i in range(100000):
    t = (i*(i+1))//2
    if t in p and t in h:
        print(i)
        print(t)