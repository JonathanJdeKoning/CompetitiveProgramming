s = input()

emp = 0
a = 0
b = 0
c = 0
ab = 0
bc = 0
ac = 0

total = 0

for x in s:
    if x=="A":
        if bc:
            bc -= 1
            emp += 1
        elif b:
            b -= 1
            ab += 1
        elif c:
            c -= 1
            ac += 1
        elif emp:
            emp -= 1
            a+= 1
        else:
            a+= 1
            total += 1

    elif x == "B":
        if ac:
            ac -= 1
            emp += 1
        elif a:
            a -= 1
            ab+= 1
        elif c:
            c-=1
            bc+= 1
        elif emp:
            b +=1
            emp -= 1
        else:
            b+=1
            total += 1

    elif x == "C":
        if ab:
            ab -= 1
            emp += 1
        elif a:
            a -= 1
            ac+= 1
        elif b:
            b -= 1
            bc+= 1
        elif emp:
            c+=1
            emp -= 1
        else:
            c += 1
            total+=1
print(total)


