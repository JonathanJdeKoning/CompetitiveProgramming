n, k = map(int, input().split())
total = 0
for _ in range(n):
    box = input().split()
    total += len(box) - len(set(box))
print(total)
