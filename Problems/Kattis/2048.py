from itertools import pairwise
mat = []
for _ in range(4):
    mat.append(list(map(int, input().split())))

newmat = []
dir = int(input())
if dir ==0 or dir==2:
    for row in mat:
        new = []
        for a, b in pairwise([x for x in row if x]):
            if a==b: new.append(a+b)
            else:
                new.append(a)
                new.append(b)
        if dir == 0:
            new.extend([0]*(4-len(new)))
            newmat.append(new)

for row in newmat:
    print(row)
