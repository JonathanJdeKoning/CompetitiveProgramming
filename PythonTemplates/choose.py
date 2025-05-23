def choose(n, k, mod=10**9+7):
    res = 1
    for i in range(1, k+1):
        res = res*i % mod
    res = pow(res, mod-2, mod)
    for i in range(n, n-k, -1):
        res = res*i % mod
    return res