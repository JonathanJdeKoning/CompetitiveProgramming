a = input()
b = input()
c = int(a) + int(b)

if int(a.replace("0", "")) + int(b.replace("0", "")) == int(str(c).replace("0","")):
    print("YES")
else:
    print("NO")
