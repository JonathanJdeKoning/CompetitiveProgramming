mod = 1000000007
from math import factorial
def inverse(n):
    return pow(n, -1, 1000000007)
qs = []
mxn = 0
for _ in range(1):
    n,k = list(map(int, input().split()))
    qs.append((n,k))
    mxn = max(mxn, n)
fac=[1]
for i in range(1, mxn+1):
    fac.append(fac[i - 1] * i % mod)

for n,k in qs:
    print(fac[n]*inverse(fac[k]*fac[n-k]%mod)  % mod)