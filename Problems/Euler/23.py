from functools import reduce

factors = lambda n: set(
    reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
)
mx = 28124
abun = set()


def f(n):
    x = factors(n)
    x.discard(n)
    return sum(x)


for i in range(1, mx):
    if f(i) > i:
        abun.add(i)
ans = 0
labun = sorted(list(abun))

for i in range(1, mx):
    found = False
    for a in labun:
        if a > i:
            break
        comp = i - a
        if comp in abun:
            found = True
            break
    if not found:
        ans += i
print(ans)
