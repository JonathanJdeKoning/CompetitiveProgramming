n, k = map(int, input().split())

plain = []
spots = []
for i in range(k):
    plain.append(set())
    spots.append((set()))
for _ in range(n):
    s = input()
    for i,c in enumerate(s):
        plain[i].add(c)

for _ in range(n):
    s = input()
    for i, c in enumerate(s):
        spots[i].add(c)

ans = 0
print(plain)
print(spots)
for i in range(k):
    if not plain[i].intersection(spots[i]): ans += 1
print(ans)
