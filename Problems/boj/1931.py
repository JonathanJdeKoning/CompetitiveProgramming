n = int(input())
times = []
for _ in range(n):
    s, e = map(int, input().split())
    times.append((s,e))
times.sort(key=lambda x:(x[1],x[0]))
print(times)
total = 0
p = 0
for s, e in times:
    if s >= p:
        total += 1
        p = e
print(total)

