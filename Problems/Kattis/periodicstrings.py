s = input()
from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

facts = sorted(factors(len(s)))
def chunks(L, n):
    for i in range(0, len(L), n):
        yield L[i:i+n]
for fact in facts:
    ck = list(chunks(s, fact))
    base = ck[0]
    for c in ck[1:]:
        if c != base[-1] + base[:-1]:
            break
        base = base[-1] + base[:-1]
    else:
        exit(print(fact))
