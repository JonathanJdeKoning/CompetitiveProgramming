from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def d(n):
    try:
        f = factors(n)
    except:
        f = set()
    f.discard(n)
    if not f: return 0
    return sum(f)
ans = set()
for a in range(1, 10001):
    b = d(a)
    if b == a: continue
    aa = d(b)

    if aa == a:
        ans.add(a)
        if b < 10000:
            ans.add(b)

print(sum(ans))
