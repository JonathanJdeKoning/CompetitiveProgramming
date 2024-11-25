from itertools import accumulate
ans = set()
mx = 10000
sq = [x**2 for x in range(1,mx+1)]
pref = [0]
pref.extend(list(accumulate(sq)))
for i in range(mx+1):
    if i%250==0: print(f"###{i}###")
    for j in range(i+2, mx+1):
        x = pref[j] - pref[i]
        if str(x) == str(x)[::-1] and x< 100000000:
            print(x)
            ans.add(x)

print(len(ans))
print(sum(ans))