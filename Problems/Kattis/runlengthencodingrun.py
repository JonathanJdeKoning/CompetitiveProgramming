from itertools import groupby
data = input().split()

op = data[0]
string = data[1]

if op == "D":
    new = ""
    for idx, c in enumerate(string):
        if c.isdigit():
            new+=string[idx-1]*int(c)
    print(new)
else:
    newdata = ["".join(g) for _, g in groupby(string)]
    new = ""
    for item in newdata:
        new+=item[0]
        new+=str(len(item))
    print(new)
    
