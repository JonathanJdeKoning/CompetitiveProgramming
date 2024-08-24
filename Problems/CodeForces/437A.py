d = {}

for _ in range(4):
    s = input()
    d[s[0]] = len(s)-2

great = []

items = list(d.items())
print(items)
for i, (k,v) in enumerate(items):
    others = items[:i] + items[i+1:]
    print(others)
    if v>= max([x[1] for x in others])*2 or v <= min([x[1] for x in others])/2:
        great.append(k)

if len(great) != 1:
    print("C")
else:
    print(great[0])

