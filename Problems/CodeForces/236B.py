from functools import reduce, cache

@cache
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

a,b,c = map(int, input().split())
ans = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            x = i*j*k
            #print(x)
            ans += len(factors(x))

print(ans%(2**30))
