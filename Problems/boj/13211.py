seen = set()
for _ in range(int(input())):
    seen.add(input())
total = 0
for _ in range(int(input())):
    if input() in seen: total += 1
print(total)
