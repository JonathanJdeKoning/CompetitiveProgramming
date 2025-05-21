from collections import defaultdict
ans = 0
s = input()
mp = defaultdict(list)
for i, c in enumerate(s):
    mp[c].append(i)

for i, a in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:-1]):
    for j, b in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i+1:], start=i+1):
        amn, amx = mp[a]
        bmn, bmx = mp[b]
        if (bmn < amn and (amn<bmx<amx)) or ((amn<bmn<amx) and bmx > amx):
            ans += 1
print(ans)

