mxChain = 0
chainNum = None
bigseen = set([1])

from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prop(n):
    f = factors(n)
    f.discard(n)
    return sum(f)

for i in range(2,1000001):
    if i%10000==0: print(i, mxChain)

    seen = set()
    num = i
    while True:
        new = prop(num)
        if new > 1000000 or new == 1: break
        if new == i:
            chainLength = len(seen)
            if chainLength > mxChain:
                mxChain = chainLength
                print()
                print(mxChain)
                print([i] + list(seen))
        if new in seen: break
        seen.add(new)
        num = new




