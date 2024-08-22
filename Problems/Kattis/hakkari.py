R, C = map(int, input().split())
mat = [list(input()) for _ in range(R)]

out = []
for i, row in enumerate(mat, start=1):
    for j, cell in enumerate(row, start=1):
        if cell == "*":
            out.append((i,j))

print(len(out))
for y,x in out:
    print(y,x)


