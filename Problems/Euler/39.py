mx = 0
best = None
for p in range(12, 1001):
    if p%50==0: print(p)
    ans = set()
    for a in range(1,p+1):
        for b in range(a, p+1):
            c = p - (a+b)

            if a**2 + b**2 == c**2:
                ans.add(tuple(sorted([a,b,c])))
    if len(ans) > mx:
        mx = len(ans)
        best = p
print(best)