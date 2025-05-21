s = input().replace(";", "$").replace(",", "$").split("$")
a = []
b = []

for chunk in s:
    if not chunk:
        b.append(chunk)
        continue
    
    for c in chunk:
        if c.isalpha() or c == ".":
            b.append(chunk)
            break
    else:
        if chunk == "0":
            a.append(chunk)
            continue
        if chunk[0] == "0":
            b.append(chunk)
            continue
        a.append(chunk)

if a:
    print(f'\"{",".join(a)}\"')
else:
    print("-")
if b:
    print(f'\"{",".join(b)}\"')
else:
    print("-")


