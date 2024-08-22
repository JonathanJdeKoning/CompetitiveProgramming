n = int(input())

s = input()
out = []

used = set()
for c in s:
    if c not in used:
        used.add(c)
        if len(used) == 3:
            out.append(c)
            used = set()
            if len(out) == n: break
print("".join(out))

