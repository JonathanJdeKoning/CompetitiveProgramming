stored = input()
test = input()

poss = [test]

for i in range(10):
    poss.append(test+str(i))
    poss.append(str(i)+test)

new = ""
for c in test:
    if c.isalpha():
        if c.islower():
            new+= c.upper()
        else:
            new+= c.lower()
    else:
        new+= c
poss.append(new)
if stored in poss:
    print("Yes")
else:
    print("No")
