n = int(input())

out = []
for i in range(n*2, n*2+n):
    out.append(i)

print(" ".join(map(str, out)))
