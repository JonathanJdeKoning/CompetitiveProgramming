n, a, b = map(int, input().split())
total = 0
for i in range(1, n+1):
    if a <= sum([int(x) for x in str(i)]) <= b:
        total += i
print(total)
