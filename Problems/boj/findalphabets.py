s = input()
out = []

for c in "abcdefghijklmnopqrstuvwxyz":
    out.append(s.find(c))

print(" ".join(map(str, out)))
