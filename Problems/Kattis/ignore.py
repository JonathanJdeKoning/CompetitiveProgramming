qs = []
while True:
    try:
        q = int(input())
    except: break
    qs.append(q)
mx = max(qs)
ans = []
curr = 1
i = 1
ups = {"1":"1", "2":"2", "5":"5", "6":"9", "8":"8","0":"0", "9":"6"}
bad = set(["3", "4", "7"])
while curr != mx+1:
    print(i)
    for j,c in enumerate(str(i)):
        if c in bad:
            i += 10**(len(str(i))-(1+j))
            break
    else:
        ans.append(i)
        curr += 1
        i+= 1


for q in qs:
    print("".join([ups[x] for x in str(ans[q-1])[::-1]]))


