imageR, imageC, kernR, kernC = map(int, input().split())

mat = []
for _ in range(imageR):
    mat.append(list(map(int, input().split())))

kern = []
for _ in range(kernR):
    kern.append(list(map(int, input().split())))

kern.reverse()
for i,row in enumerate(kern):
    kern[i] = row[::-1]
out = []
for i, row in enumerate(mat[:(imageR-kernR)+1]):
    outrow = []
    for j, cell in enumerate(row[:(imageC-kernC)+1]):
        start = 0
        for kernI, kernRow in enumerate(kern,start=i):
            for kernJ, kernCell in enumerate(kernRow,start=j):
                start += mat[kernI][kernJ]*kernCell
        outrow.append(start)
    out.append(outrow)

for row in out:
    print(" ".join([str(x) for x in row]))



