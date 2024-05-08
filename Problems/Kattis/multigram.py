from functools import reduce
s = input()
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
mn = len(s)
for factor in sorted(list(factors(len(s)))):
    chunk = sorted(s[0:factor])
    bad = False
    for i in range(factor,len(s),factor):
        new = sorted(s[i:i+factor])
        if new != chunk:
            bad = True
            break
    if bad: continue
    if factor == len(s):
        print(-1)
        break
    print(s[:factor])
    break
