from math import factorial
mxChain = 0
chainNum = None
bigseen = set([1])

def prop(n):
    return sum([factorial(int(x)) for x in str(n)])
ans = 0 
for i in range(2,1000001):
    if i%10000==0: print(i, mxChain)

    seen = set()
    num = i
    while True:
        new = prop(num)
        if new > 1000000 or new == 1: break
        if new in seen:
            chainLength = len(seen)
            if chainLength == 59:
                ans += 1
                print(ans)
        if new in seen: break
        seen.add(new)
        num = new




