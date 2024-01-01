n, m = list(map(int, input().split()))

dance = []

for row in range(n):
    dance.append(list(input()))

rotated = list(zip(*dance[::-1]))

count = 1
for row in rotated:
    if row.count("_") == n:
        count += 1
print(count)