n, qs = map(int, input().split())

d = {}
for _ in range(n):
    site, p = input().split()
    d[site] = p

for _ in range(qs):
    print(d[input()])
