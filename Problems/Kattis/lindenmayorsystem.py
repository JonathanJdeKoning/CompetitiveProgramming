n, m = map(int, input().split())

d = {}

for _ in range(n):
    data = input().split()
    d[data[0]] = data[2]

start = input()



for _ in range(m):
    out = []
    for c in start:
        out.append(d.get(c,c))
    start = "".join(out)

print(start)
