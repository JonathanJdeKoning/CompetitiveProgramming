s = input().replace(","," ")
out = []
for c in s:
    if c == " ": out.append(" ");continue
    if c.islower(): out.append(c.upper())
    else:
        out.append(c.lower())
print("".join(out))
