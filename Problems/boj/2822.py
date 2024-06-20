import heapq

h = []
for i in range(1,9):
    heapq.heappush(h, (-int(input()), i))

out = []
tot = 0
for i in range(5):
    val, idx = heapq.heappop(h)
    tot += val
    out.append(idx)

print(abs(tot))
print(" ".join(map(str, sorted(out))))
