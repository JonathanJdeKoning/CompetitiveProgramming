sentence = input()
start = sentence[0]
out = [start]
for c in sentence[1:]:
    if c == start:
        continue
    else:
        out.append(c)
        start = c
print("".join(out))
        
