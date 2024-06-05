topl = 8
topr = 8
botl = 8
botr = 8
tr = True
tl = True
br = True
bl = True

for _ in range(int(input())):
    tooth, status = input().split()
    if status == "b":
        if tooth[0] == "+": tl = False
        elif tooth[0] == "-": bl = False
        elif tooth[1] == "+": tr = False
        elif tooth[1] == "-": br = False

    elif status == "m":
        if tooth[0] == "+": topl -= 1
        elif tooth[0] == "-": botl -= 1 
        elif tooth[1] == "+": topr -= 1
        elif tooth[1] == "-": botr -= 1

if topl == 0: tl = False
if topr == 0: tr = False
if botl == 0: bl = False
if botr == 0: br = False

if tl and bl:
    print("0")
elif tr and br:
    print("1")
else:
    print("2")





