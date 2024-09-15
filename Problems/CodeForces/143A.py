r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())


for a in range(1,10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if len(set([a,b,c,d])) != 4: continue
                if a+b == r1 and c+d == r2 and a+c == c1 and b+d == c2 and a+d ==d1 and b+c == d2:
                    exit(print(f"{a} {b}\n{c} {d}"))

print(-1)
