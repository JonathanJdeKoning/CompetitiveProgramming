N = int(input())
thore = "ThoreHusfeldt"
names = [input() for _ in range(N)]
if names[0] == thore: exit(print("Thore is awesome"))
idx = names.index(thore)
names = names[:idx]
for name in names:
    if name.startswith("ThoreHusfeld"): exit(print("Thore sucks"))
mx = 0
for name in names:
    for i,c in enumerate(name):
        if thore[i] != c:
            mx = max(mx, i)
            break
        mx = max(mx, i+1)

print(thore[:mx+1])