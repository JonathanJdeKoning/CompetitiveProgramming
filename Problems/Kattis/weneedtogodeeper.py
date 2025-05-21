N = int(input())

ans = 0 
for w in range(4, 24):
    for h in range(5, 24):
        x = w + w + (h-2) + (h-2)
        if x <= N:
            ans += 1
print(ans)