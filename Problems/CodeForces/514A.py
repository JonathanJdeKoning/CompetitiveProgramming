s = input()
out =[]

for i, c in enumerate(s):
    if i==0 and c == "9":
        out.append("9")
        continue
    a = int(c)
    b = 9-a
    out.append(str(min(a,b)))

print("".join(out))
