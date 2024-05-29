s,e = map(int, input().split())
out = []
for i in range(s,e+1):
    x = str(i)
    if len([z for z in x if z not in "47"]) !=0: continue
    out.append(x)

print(" ".join(out)) if out else print(-1)
