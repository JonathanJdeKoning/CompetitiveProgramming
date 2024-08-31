key = "".join({k:None for k in input()}.keys()).replace(" ","")
alph = []
for c in "abcdefghijklmnoprstuvwxyz":
    if c not in key: alph.append(c)
alph = list((key+ "".join(alph)))
text = input().replace(" ","") +"$"
loc = {}
mat = [
    alph[:5],
    alph[5:10],
    alph[10:15],
    alph[15:20],
    alph[20:]
]
out = []
for i, row in enumerate(mat):
    #print(row)
    for j, cell in enumerate(row):
        loc[cell] = (i,j)
#print(text)
curr = 0

while True:
    if text[curr] == "$": break
    currAdd = 2
    a,b = text[curr], text[curr+1]
    
    if a == b or b == "$":
        b = "x"
        currAdd = 1


    aY, aX = loc[a]
    bY, bX = loc[b]

    #print(a,b)
    if aY == bY:
        out.append(mat[aY][(aX+1)%5])
        out.append(mat[bY][(bX+1)%5])

    elif aX == bX:
        out.append(mat[(aY+1)%5][aX])
        out.append(mat[(bY+1)%5][bX])

    else:
        out.append(mat[aY][bX])
        out.append(mat[bY][aX])
    curr += currAdd
print("".join(out).upper())
