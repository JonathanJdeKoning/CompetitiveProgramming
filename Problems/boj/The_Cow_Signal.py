R, C, k = list(map(int, input().replace(","," ").split()))
mat = [list(input()) for _ in range( R )]
new = []

for row in mat:
    newrow = []
    for c in row:
        for _ in range(k):
            newrow.append(c)
    for _ in range(k):
        new.append(newrow)

print("\n".join(["".join(map(str, row)) for row in new ]))

