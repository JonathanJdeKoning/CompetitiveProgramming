n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]

good = set(list(range(1, n+1)))
for i,row in enumerate(mat):
    for j, res in enumerate(row):
        if res == 1:
            good.discard(i+1)
        elif res == 2:
            good.discard(j+1)
        elif res == 3:
            good.discard(i+1)
            good.discard(j+1)
print(len(good))
g = sorted(list(good))

print(" ".join(map(str, g)))

