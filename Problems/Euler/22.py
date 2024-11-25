from mynames import names
ans = []
names.sort()
ans = 0

for i, name in enumerate(names, start=1):
    ans += i*(sum([ord(x)-64 for x in name]))

print(ans)
