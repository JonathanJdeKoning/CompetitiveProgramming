a , b = input().split()
chr = "" 
for i, c in enumerate(a):
    if c in b:
        chr = c
        break


ai = a.index(chr)
bi = b.index(chr)

mat = []
for y in range(len(b)):
    out = ""
    for x in range(len(a)):
        if x!=ai:
            out+= "."
        else:
            out+=b[y]
    mat.append(out)

mat[bi] = a

for row in mat:
    print(row)
