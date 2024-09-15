n = int(input())
ans = 0

for i in range(1, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if i+j+k+l == n:
                    ans += 1

print(ans)
