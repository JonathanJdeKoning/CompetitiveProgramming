s = input()
r = 0
total = 0
for c in s:
    if c == ">":
        r += 1
    elif c == "<":
        total += r
print(total)
