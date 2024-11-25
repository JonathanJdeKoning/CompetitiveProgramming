from math import factorial
def f(n,r):
    N = factorial(n)
    R = factorial(r)
    return N//(R*factorial((n-r)))
ans = 0
for n in range(1,101):
    for r in range(1,n+1):
        if f(n,r) > 1000000:
            ans += 1

print(ans)