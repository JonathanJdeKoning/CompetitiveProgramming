r, c = list(map(int, input().split()))

top = ["#" for x in range(c+2)]
mat = [top]
for _ in range(r):
    mat.append(["#"] + list(input()) + ["#"])
mat.append(top)

words = []

for row in mat:
    rowstr = "".join(x[0] for x in row)
    
    build = ""
    for c in rowstr:
        if c.isalpha():
            build+= c
        else:
            if len(build)>1:
                words.append(build)
            build = ""


mat = list(zip(*mat))[::-1]
for row in mat:
    rowstr = "".join(x[0] for x in row)
    
    build = ""
    for c in rowstr:
        if c.isalpha():
            build+= c
        else:
            if len(build)>1:
                words.append(build)
            build = ""




print(sorted(words)[0])
