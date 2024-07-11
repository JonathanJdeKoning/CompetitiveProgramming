R, C = map(int, input().split())
u,l,r,d = map(int, input().split())
mat = [list(input()) for _ in range(R)]
width = l+r+C
new = []
i=-1
j=R
for i in range(u):
    row = []
    for j in range(width):
        if (i+j)%2==0:
            row.append("#")
        else:
            row.append(".")
    new.append(row)

for j, row in enumerate(mat,start=i+1):
    newrow = []
    k=-1
    for k in range(l):
        if (j+k)%2==0:
            newrow.append("#")
        else:
            newrow.append(".")
    newrow.extend(row)
    for m in range(k+1+len(row),len(row)+k+1+r):
        if (j+m)%2==0:
            newrow.append("#")
        else:
            newrow.append(".")
    new.append(newrow)

for i in range(j+1,d+j+1):
    row = []
    for n in range(width):
        if (i+n)%2==0:
            row.append("#")
        else:
            row.append(".")
    new.append(row)

for row in new:
    print("".join(row))



