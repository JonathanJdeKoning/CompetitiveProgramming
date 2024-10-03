N =int(input())
seen = {}
mx = 0
best = None
for _ in range(N):
    x, s = input().split()
    x = int(x)

    for c in s:
        if c not in seen:
            seen[c] = x
        else:
            dist = x - seen[c]
            if dist > mx:
                mx = dist
                best = c
            seen[c] = x
print(best)

