new = []
R, C = map(int, input().split())
mat = []
for _ in range(R):
    mat.append(list(input()))



mat = list(zip(*mat[::-1]))

for row in mat:
    new.append(list(sorted(row)))

new = list(zip(*new[::-1]))

for row in new:
    print("".join(row[::-1]))
