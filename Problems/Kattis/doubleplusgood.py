s = input()
p = s.count("+")
s = s.split("+")
res = set()

for i in range(2**p):
    rule = bin(i)[2:].zfill(p)
    base = s[0]
    for j in range(len(rule)):
        if rule[j] == "1":
            base = str(base) + str(s[j+1])
        else:
            base = int(base) + int(s[j+1])

    res.add(int(base))
print(res)
print(len(res))


