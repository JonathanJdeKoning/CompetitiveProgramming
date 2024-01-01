total = 0
mat = []
for i in range(7):
    s = input()
    total+= s.count("oo.")
    total += s.count(".oo")
    mat.append([c for c in s])
mat = list(zip(*mat[::-1]))
for row in mat:
    s = "".join(row)
    total += s.count("oo.")
    total += s.count(".oo")
print(total)
