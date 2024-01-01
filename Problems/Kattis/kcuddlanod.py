x, y = input().split()
x = x[::-1]
y = y[::-1]

newx = ""
newy = ""

for c in x:
    if c == "2":
        newx += "5"
    elif c == "5":
        newx += "2"
    else:
        newx += c

for c in y:
    if c == "2":
        newy += "5"
    elif c == "5":
        newy += "2"
    else:
        newy += c

if int(newx) > int(newy):
    print(1)
else:
    print(2)
