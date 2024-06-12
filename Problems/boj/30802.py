n = int(input())
sizes = list(map(int, input().split()))
t,p = map(int, input().split())

total = 0
for size in sizes:
    div, rem = divmod(size, t)
    total += div
    if rem: total += 1

print(total)

print(*divmod(n, p))
