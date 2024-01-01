s = input()
tot = 0
for i,c in enumerate(s):
    if c == ">":
        tot+= s[i:].count("<")
print(tot)
