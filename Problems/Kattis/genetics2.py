n,m,k = map(int, input().split())
s = [input() for x in range(n)]
for i, x in enumerate(s):
    total = 0
    for y in s:
        if len([z for z in range(len(y)) if y[z] != x[z]]) == k:
            total += 1
    if total == n-1:
        print(i+1)
