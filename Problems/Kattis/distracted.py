peeps, qs = map(int, input().split())
m = set()
u = set()
q = set()
for _ in range(peeps):
    name, stat = input().split()
    if stat == "m": m.add(name)
    if stat == "u": u.add(name)
    if stat == "?": q.add(name)

ans = "0"
for _ in range(qs):
    look, x, see = input().split()
    if look in u or see in m: continue

    if look in q or see in q:
        ans = "?"
        continue
    
    ans = "1"
    break
    
print(ans)
