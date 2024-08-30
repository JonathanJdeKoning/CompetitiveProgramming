from math import inf, ceil, floor
k, r = map(int, input().split())
have = list(map(int, input().split()))
mx = 0
for _ in range(r):
    data = list(map(int, input().split()))
    mxSmoothies = inf
    for ing, amount in enumerate(data[:-1]):
        stock = have[ing]
        if amount and not stock: break
        if not amount: continue
        mxSmoothies = min(mxSmoothies, stock//amount)
    mx = max(mx, mxSmoothies*data[-1])
print(mx)

