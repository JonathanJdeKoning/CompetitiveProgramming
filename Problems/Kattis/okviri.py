s = input()

final = []
out = ".."
for i in range(1,len(s)+1):
    if (i)%3==0:
        out+= "*"
    else:
        out += "#"
    out+= "..."
final.append(out[:-1])

out = "."
for i in range(1,len(s)+1):
    if (i)%3==0:
        out += "*.*."
    else:
        out += "#.#."
final.append(out)

out = ""
for i in range(1,len(s)+1):
    if(i)%3 == 0 or (i-1)%3==0 and i-1!= 0:
        out+= f"*.{s[i-1]}."
    else:
        out += f"#.{s[i-1]}."
if i%3!= 0:
    out += "#"
else:
    out += "*"
final.append(out)


out = "."
for i in range(1,len(s)+1):
    if (i)%3==0:
        out += "*.*."
    else:
        out += "#.#."
final.append(out)

out = ".."
for i in range(1,len(s)+1):
    if (i)%3==0:
        out+= "*"
    else:
        out += "#"
    out+= "..."
final.append(out[:-1])


print("\n".join(final))
